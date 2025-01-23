from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def home(request):
    return HttpResponse("BYE BYyE")


class GetEndpoint1(APIView):
    def get(self, request):
        data = {"message": "First GET"}
        return Response(data)

class GetEndpoint2(APIView):
    def get(self, request):
        data = {"message": "The second one GET"}
        return Response(data)

class PostEndpoint(APIView):
    def post(self, request):
        received_data = request.data
        data = {"message": "POST request received", "received_data": received_data}
        return Response(data, status=status.HTTP_201_CREATED)