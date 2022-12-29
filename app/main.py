import torch
from fastapi import FastAPI
from .utility import inference
from pydantic import BaseModel, Field
from typing import Union, List

app = FastAPI()

class DetectedObject(BaseModel):
    xmin: float
    ymin: float
    xmax: float
    ymax: float
    confidence: float
    detected_class: int = Field(alias='class')
    name: str

class DetectionResponse(BaseModel):
    detected_objects: List[DetectedObject]

@app.get("/")
def read_root():
    return {"message": "you are here for a reason, follow your heart."}

# main endpoint for object detection using yolo5 small model
@app.get("/detect_objects", response_model=DetectionResponse)
async def detect(image_url:str):
    objects = inference(image_url)
    return {"detected_objects": objects}