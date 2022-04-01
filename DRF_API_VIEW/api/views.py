
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
class StudentAPI(APIView):
    def get(self, id=None):
        id = id
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data is created'}
            return Response(res, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

    def put(self, request,id):
        id=id
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data is updated'}
            return Response(res,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
            
    def patch(self, request,id):
        id=id
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data is partially updated'}
            return Response(res)
        else:
            return Response(serializer.errors)

        
    def delete(self,id):
        id=id
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'Data Deleted'}
        return Response(res)