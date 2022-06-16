import validators
import cv2

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from tesseract.routers.helper import download_image

router = APIRouter(
    prefix="/tesseract", tags=["tesseract"], responses={404: {"description": "Not found"}}
)

# ---
#  Tesseract
# ---


class OCRImage(BaseModel):
    url: str


@router.post("/ocr")
async def tesseract_process(image: OCRImage):
    if not validators.url(image.url):
        raise HTTPException(status_code=400, detail="invalid image url")

    image = await download_image(image.url)

    cv2.imwrite("test.png", image)

    print("image test fun!")

    return image
