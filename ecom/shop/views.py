
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import*
from.serializers import *

@api_view(['GET'])
def home(request):
    Products_obj=Products.objects.all()
    serializer=Products.Serializer(Products_obj,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def post_Products(request):
     data=request.data
     print(data)
     return Response(data)