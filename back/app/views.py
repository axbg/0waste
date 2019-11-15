import json 
import base64

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2
import io
import PIL
from PIL import Image
import cv2
import numpy as np

# Create your views here.
def get_color_by_type(type):
    return (0, 0, 0)
def get_credentials():
    return ["849576898441", "IOD3355942584437440512"]

def callVision(content):
    prediction_client = automl_v1beta1.PredictionServiceClient()
    [project_id, model_id] = get_credentials()
    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    payload = {'image': {'image_bytes': content }}
    params = {}
    request = prediction_client.predict(name, payload, params)
    return request

def splashImage(img):
    content = img.read()

    image = Image.open(io.BytesIO(content))
    width, height = image.size
    
    #make it gray-scale
    processed_image = np.asarray(image)[:,:,::-1].copy()
    annotations = callVision(content)
    ct = 0
    for mark in annotations.payload:
        ct = ct + 1
        [upper, lower] = mark.image_object_detection.bounding_box.normalized_vertices
        start_point = (int(width * upper.x), int(height * upper.y))
        end_point = (int(width * lower.x), int(height * lower.y))
        color = get_color_by_type(mark.display_name)
        thickness = 10
        processed_image = cv2.rectangle(processed_image, start_point, end_point, color, thickness)

    retval, buffer = cv2.imencode('.jpg', processed_image)
    b64img = base64.b64encode(buffer)
    return [b64img, ct]
                

class AppRoot(APIView):
    def get(self, request):
        message = "hello"
        return Response(message)

class FastTrackEndpoint(APIView):
    def post(self, request):
        photos = request.FILES.getlist('photos')
        images = []
        objects = []

        for photo in photos:
            with photo.open("rb") as img:
                [image, objs] = splashImage(img)
                images.append(image)
                objects.append(objs)

        return Response({"annotated": images, "objects": objects})

class ImpactMeasurementEndpoint(APIView):
    def post(self, request):
        print(request.data)
        return Response("yas")

class CatalogueEndpoint(APIView):
    def get(self, request):
        
        return Response("yz")