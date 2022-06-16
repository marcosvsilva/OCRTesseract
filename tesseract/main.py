from fastapi import FastAPI

from tesseract.routers import tesseract

app = FastAPI()

# app.include_router(nlp.router)
app.include_router(tesseract.router)


@app.get("/")
async def root():
    return {"message": "hello"}
