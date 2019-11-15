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
from .models import FastTrack

# Create your views here.
def get_color_by_type(waste_type):
    if(waste_type == "bag"):
        #bag - orange
        return (0, 165, 255)
    elif(waste_type == "bottle"):
        #bottle - red
        return (0, 0, 255)
    elif(waste_type == "cap"):
        #cap - blue
        return (255, 0, 0)
    elif(waste_type == "rope"):
        #rope - green
        return (50, 205, 50)
    else:
        #waste - yellow
        return (0, 255, 255)
            
def get_credentials():
    return ["849576898441", "IOD3355942584437440512"]

def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

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
    
    processed_image = np.asarray(image)[:,:,::-1].copy()
    greyscale_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2GRAY)
    greyscale_image = cv2.cvtColor(greyscale_image, cv2.COLOR_GRAY2RGB)
    greyscale_image = increase_brightness(greyscale_image, 100)

    annotations = callVision(content)
    ct = 0
    for mark in annotations.payload:
        ct = ct + 1
        [upper, lower] = mark.image_object_detection.bounding_box.normalized_vertices
        start_point = (int(width * upper.x), int(height * upper.y))
        end_point = (int(width * lower.x), int(height * lower.y))
        color = get_color_by_type(mark.display_name)
        thickness = 10
        colored_cut = processed_image[int(height * upper.y):int(height * lower.y),  int(width * upper.x):int(width * lower.x)]
        greyscale_image[int(height * upper.y):int(height * lower.y),  int(width * upper.x):int(width * lower.x)] = colored_cut
        greyscale_image = cv2.rectangle(greyscale_image, start_point, end_point, color, thickness)

    retval, buffer = cv2.imencode('.jpg', greyscale_image)
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
                log = FastTrack(raw="", annotated=image)
                log.save()

        return Response({"annotated": images, "objects": objects})

class ImpactMeasurementEndpoint(APIView):
    def post(self, request):
        before = request.FILES.getlist('before')
        after = request.FILES.getlist('after')

        beforeImages = []
        afterImages = []
        beforeObjects = []
        afterObjects = []

        for i in range(0, len(before)):
            with before[i].open("rb") as img:
                [image, objs] = splashImage(img)
                beforeImages.append(image)
                beforeObjects.append(objs)
                log = FastTrack(raw="", annotated=image)
                log.save()
            
            with after[i].open("rb") as img:
                [image, objs] = splashImage(img)
                afterImages.append(image)
                afterObjects.append(objs)
                log = FastTrack(raw="", annotated=image)
                log.save()

        return Response({"beforeImages": beforeImages, "afterImages": afterImages, "beforeObjects": beforeObjects, "afterObjects": afterObjects})

class CatalogueEndpoint(APIView):
    def get(self, request):
        logs = FastTrack.objects.all()
        annotated = []
        for log in logs:
            annotated.append((log.annotated[2:])[:-1])
        return Response({"photos": annotated})