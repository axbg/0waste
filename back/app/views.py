import io
import PIL
import cv2
import json 
import base64


from .models import FastTrack
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from google.cloud.automl_v1beta1.proto import service_pb2
from .utils import get_color_by_type, get_credentials, increase_brightness, callVision, splashImage

              
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