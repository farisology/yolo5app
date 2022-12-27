import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

"""
Loading the model, this is kept out of the method to avoid loading the model with every request.
The method is simple, reading image url and the model in torch takes care of subprocesses.
The module is kept separate from the endpoint to keep neat code by seapration of logic.
"""
def inference(image_address):
    # Inference
    results = model([image_address])
    objects_dic = list() # Detected objects data are added into list
    for row in results.pandas().xyxy[0].iterrows(): # iterating over the objects of one image
        objects_dic.append(dict(row[1]))

    return objects_dic