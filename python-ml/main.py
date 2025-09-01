from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from transformers import pipeline
from PIL import Image
import io

app = FastAPI()

nsfw_model = None

@app.on_event("startup")
async def load_model():
    global nsfw_model
    nsfw_model = pipeline("image-classification", model="Falconsai/nsfw_image_detection", use_fast=True)
    print("NSFW model loaded and ready!")

def check_nsfw(image_bytes: bytes) -> bool:
    image = Image.open(io.BytesIO(image_bytes))
    results = nsfw_model(image)
    print("Model results:", results)
    return any(r["label"].lower() in ["porn", "hentai", "nsfw", "sexy"] and r["score"] > 0.7 for r in results)

@app.post("/api/blog/check")
async def add_blog(image: UploadFile = File(...)):
    image_bytes = await image.read()

    if check_nsfw(image_bytes):
        return {"success": False, "detail":"Inappropriate image detected."}

    return {"success": True, "message": "Image is appropriate"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
