import fitz

from fitz import Document, Page
from pydantic import BaseModel, Field
from typing import Literal

from mediqbox.loadpdf.rect import *

class Image(BaseModel):
  number: int
  bbox: tuple[float, float, float, float]
  width: int
  height: int
  cs_name: str = Field(alias="cs-name")
  colorspace: int
  xres: int           # resolution in x-direction
  yres: int           # resolution in y-direction
  bpc: int            # bits per component
  size: int           # storage occupied by image
  digest: bytes       # MD5 hashcode
  xref: int           # image xref or 0

class Drawing(BaseModel):
  type_: Literal["f", "s", "fs"] = Field(alias="type")
  bbox: tuple[float, float, float, float] = Field(alias="rect")

def get_images(
    page: Page
) -> list[Image]:
  return [Image.model_validate(img)
          for img in page.get_image_info(xrefs=True) if img.get('xref', 0)]

def get_drawings(
    page: Page
) -> list[Drawing]:
  return [Drawing.model_validate(drw)
          for drw in page.get_cdrawings()]

def recoverpix(
    doc: Document,
    xref: int,
    smask: int
) -> dict:
  """
  Extract an image of a document.

  https://github.com/pymupdf/PyMuPDF-Utilities/blob/master/examples/extract-images/extract-from-pages.py

  :param xref: xref of PDF image
  :param smask: xref the its /SMask
  :return: dictionary of the image data
  """
  # special case: /SMask or /Mast exists
  if smask > 0:
    pix0 = fitz.Pixmap(doc.extract_image(xref)["image"])
    if pix0.alpha: # catch irregular situation
      pix0 = fitz.Pixmap(pix0, 0) # remove alpha channel
    mask = fitz.Pixmap(doc.extract_image(smask)["image"])

    try:
      pix = fitz.Pixmap(pix0, mask)
    except: # fallback to original base image in case of problems
      pix = fitz.Pixmap(doc.extract_image(xref)["image"])

    if pix0.n > 3:
      ext = "pam"
    else:
      ext = "png"

    return { # create dictionary expected by caller
      "ext": ext,
      "colorspace": pix.colorspace.n,
      "image": pix.tobytes(ext)}
  
  # special case: /Colorspace definition exists
  # to be sure, we convert these cases to RGB PNG images
  if "/Colorspace" in doc.xref_object(xref, compressed=True):
    pix = fitz.Pixmap(doc, xref)
    pix = fitz.Pixmap(fitz.csRGB, pix)
    return { # create dictionary expected by caller
      "ext": "png",
      "colorspace": 3,
      "image": pix.tobytes("png")}
  
  return doc.extract_image(xref)