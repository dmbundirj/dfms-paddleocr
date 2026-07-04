from fastapi import FastAPI

app = FastAPI(
    title="DFMS PaddleOCR API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "status": "success",
        "message": "DFMS OCR API Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
