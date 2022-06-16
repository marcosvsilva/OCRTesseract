import requests
import numpy as np
import cv2

from fastapi import HTTPException


async def download_image(image_url: str) -> np.ndarray:
    stream = await download_file(image_url)

    if stream is None:
        raise HTTPException(status_code=400, detail="no image content")

    jpg_to_np = np.frombuffer(stream, np.uint8)
    result = cv2.imdecode(jpg_to_np, flags=1)

    return result


async def download_file(url: str, as_stream=True):
    req = requests.get(url, stream=as_stream)

    if req.status_code == 200:
        result = req.content
    else:
        raise HTTPException(status_code=400, detail="invalid url")

    return result
