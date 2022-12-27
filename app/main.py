import torch
from fastapi import FastAPI
from .utility import inference
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "you are here for a reason, follow your heart."}

# main endpoint for object detection using yolo5 small model
@app.get("/detect_objects")
async def detect(image_url:str):
    objects = inference(image_url)
    return {"detected_objects": objects}