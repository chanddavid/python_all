
from functools import partial
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
    
@csrf_exempt
def getdata(request):
    if request.method=='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        id=parsed_data.get('id')
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return JsonResponse(serializer.data)

        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data is created'}
            return JsonResponse(res)
        else:
            return JsonResponse(serializer.errors)

    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        id=parsed_data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data is updated'}
            return JsonResponse(res)
        else:
            return JsonResponse(serializer.errors)
        
    if request.method=='PATCH':
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        id=parsed_data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=parsed_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data is partially updated'}
            return JsonResponse(res)
        else:
            return JsonResponse(serializer.errors)

    
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        id=parsed_data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'Data Deleted'}
        return JsonResponse(res)
        

        


    