import json 
import base64
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class AppRoot(APIView):
    def get(self, request):
        message = "hello"
        return Response(message)

class FastTrackEndpoint(APIView):
    def post(self, request):
        print(request.data['raw'])

        for image in request.data['raw']:
            print(image["image"])
            
        # imgdata = base64.b64decode(request.data['raw'])
        # filename = 'some_image.jpg' 
        # with open(filename, 'wb') as f:
        #     f.write(imgdata)

        return Response('ye')

class ImpactMeasurementEndpoint(APIView):
    def post(self, request):
        print(request.data)
        return Response("yas")