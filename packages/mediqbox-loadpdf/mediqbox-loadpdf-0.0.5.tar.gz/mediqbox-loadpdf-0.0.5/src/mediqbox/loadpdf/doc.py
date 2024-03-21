import os
import re

from mediqbox.loadpdf.helpers import *
from mediqbox.loadpdf.text import *
from mediqbox.loadpdf.figure import *

class ExtractedFigure(BaseModel):
  type_: Literal["figure", "table", "unknown"] = Field(alias="type")
  page_number: int
  x0: float
  y0: float
  x1: float
  y1: float
  filename: str
  label: str = ""
  caption: str = ""

def detect_caption(
    roi: Rect, 
    text_blocks: list[TextBlock],
    gap: float = 20.0
) -> tuple[str, str]:
  label, caption = "", ""

  re_caption = re.compile(
    r"(Figure|Fig|Table|Tab|表|图)\.?\s*.?\.?\s*\(?\d+\)?", flags=re.I)
  
  min_distance = gap
  for block in text_blocks:
    m = re_caption.match(block.text)
    if m:
      distance = manhattan_distance(roi, Rect(block.bbox))
      if distance == 0.0:
        return (m.group(0), block.text)
      if distance < min_distance:
        min_distance = distance
        label, caption = m.group(0), block.text
        caption = caption.replace("-\n", "-").replace("\n", " ").replace("  ", " ")
  
  return label, caption

class PdfPage(BaseModel):
  model_config = ConfigDict(arbitrary_types_allowed=True)

  page: Page

  text_blocks: list[TextBlock] = []
  images: list[Image] = []
  drawings: list[Drawing] = []

  major_text_blocks: list[TextBlock] = []

  removed_text_blocks: list[TextBlock] = []
  removed_images: list[Image] = []
  removed_drawings: list[Drawing] = []

  @property
  def pno(self) -> int:
    return self.page.number
  
  @property
  def bound(self) -> Rect:
    return self.page.bound()

  def remove_content_by_area_relations(
      self,
      area: Rect,
      content_types: set[Literal['text', 'image', 'drawing']],
      relations: set[Literal["outside", "on"]]
  ) -> None:
    if not area:
      return
    
    mapping = {
      'text': {'content_list': self.text_blocks, 'removed_content_list': self.removed_text_blocks},
      'image': {'content_list': self.images, 'removed_content_list': self.removed_images},
      'drawing': {'content_list': self.drawings, 'removed_content_list': self.removed_drawings}}
    
    for ct in content_types:
      content_list = mapping.get(ct, {}).get('content_list')
      removed_content_list = mapping.get(ct, {}).get('removed_content_list')
      
      i = 0
      while i < len(content_list):
        content = content_list[i]
        intersecting = intersect(Rect(content.bbox), area)
        if (("outside" in relations and not intersecting) or 
            ("on" in relations and intersecting)):
          removed_content_list.append(content)
          content_list.pop(i)
          continue
        i += 1

    return
  
class PdfDoc(BaseModel):
  model_config = ConfigDict(arbitrary_types_allowed=True)

  doc: Document
  file_size: int
  sha256sum: str

  pages: list[PdfPage] = []
  major_fonts: list[FontItem] = []
  major_content_area: Optional[tuple[float, float, float, float]] = None

  def __init__(self, **data):
    super().__init__(**data)

    for page in self.doc:
      self.pages.append(PdfPage(
        page = page,
        text_blocks = get_text_blocks(page),
        images = get_images(page),
        drawings = get_drawings(page)))
      
    return
  
  @property
  def page_count(self) -> int:
    return self.doc.page_count
      
  def save(self, filename: str) -> None:
    for page in self.pages:
      # remove removed_text_blocks
      for block in page.removed_text_blocks:
        page.page.add_redact_annot(block.bbox)
      # remove removed_images
      for img in page.removed_images:
        page.page.delete_image(img.xref)
      # remove removed_drawings
      for drw in page.removed_drawings:
        page.page.add_redact_annot(drw.bbox)
      
      page.page.apply_redactions(images=0)

    self.doc.save(filename)
    return

  def get_major_fonts_and_content_area(self) -> None:
    text_blocks: list[TextBlock] = []
    page_rects: list[Rect] = []

    for page in self.doc:
      text_blocks += get_text_blocks(page)
      page_rects.append(page.rect)

    if not(len(text_blocks)):
      return
    
    nlimit = max(1, 4 - self.page_count)
    self.major_fonts = [
      item for item in get_major_fonts(text_blocks, nlimit=nlimit)]

    # TODO rotate some pages to unify the page rect
    if not len(set(page_rects)) == 1:
      return
    
    major_text_blocks = find_major_font_text_blocks(
      text_blocks, self.major_fonts)
    self.major_content_area = get_bounding_rect(
      [Rect(block.bbox) for block in major_text_blocks])
    
    return
  
  def cleanse(self) -> None:
    self.get_major_fonts_and_content_area()

    for page in self.pages:
      page.remove_content_by_area_relations(
        self.major_content_area, content_types={"text", "image", "drawing"}, relations={"outside"})
      page.major_text_blocks = find_major_font_text_blocks(page.text_blocks, self.major_fonts)
      for block in page.major_text_blocks:
        page.remove_content_by_area_relations(
          Rect(block.bbox), content_types={"image"}, relations={"on"})
        
  def extract_figures(
      self,
      figure_dir: str,
      min_figure_area_percentile: float = 0.1,
      scale: float = 1.0,
      epsilon: float = 3.0
  ) -> list[dict[str, Any]]:
    extracted_figures: list[ExtractedFigure] = []

    for page in self.pages:
      # Filter out dummy images (clips, etc.)
      dummy_xrefs = [img[0] for img in page.page.get_images()
                     if img[1] > 1 and img[5] == "DeviceGray"]
      images = [img for img in page.images
                if not img.colorspace == 0 and not img.xref in dummy_xrefs]
      drawings = page.drawings
      
      min_figure_area = page.bound.get_area() * min_figure_area_percentile

      # Find least bounding rectangles for images and drawings
      free_rects = find_least_bounding_rects(
        [Rect(img.bbox) for img in images] +
        [Rect(drw.bbox) for drw in drawings], merging_distance=epsilon)

      # Add text blocks intersecting with or close to the bounding rectangles
      text_rects = []
      for block in page.text_blocks:
        for rect in free_rects:
          tr = Rect(block.bbox)
          if manhattan_distance(rect, tr) <= epsilon:
            text_rects.append(tr)
            break
      
      # Find least bounding rectangles again
      free_rects = find_least_bounding_rects(
        free_rects + text_rects, merging_distance=epsilon)

      # Subtract major text blocks from the rectangles
      for block in page.major_text_blocks:
        subtract_rect(free_rects, Rect(block.bbox), min_area=min_figure_area)

      # Find least bounding rectangles again since the last step may result in fractional blocks
      free_rects = find_least_bounding_rects(
        free_rects, merging_distance=epsilon)
      
      # Filter out small pieces
      free_rects = [r for r in free_rects if r.get_area() >= min_figure_area]

      matrix = Matrix(scale, scale)
      for i in range(len(free_rects)):
        rect = free_rects[i]
        if page.page.rotation == 90:
          rect = Rect(rect.y0, rect.x0, rect.y1, rect.x1)
        pixmap = page.page.get_pixmap(
          clip=rect, matrix=matrix)
        
        filename = f"figure_{page.pno}_{i}.png"
        pixmap.save(os.path.join(figure_dir, filename))
        label, caption = detect_caption(rect, page.text_blocks)
        type_ = "unknown"
        if label.lower().startswith("fig") or label.startswith("图"):
          type_ = "figure"
        elif label.lower().startswith("tab") or label.startswith("表"):
          type_ = "table"

        extracted_figures.append(ExtractedFigure(
          label=label,
          caption=caption,
          filename=filename,
          page_number=page.pno,
          x0=rect.x0,
          y0=rect.y0,
          x1=rect.x1,
          y1=rect.y1,
          type=type_ 
        ).model_dump())

    return extracted_figures