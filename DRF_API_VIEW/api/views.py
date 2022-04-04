
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly, IsAuthenticated,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class StudentAPI(APIView):
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request, id=None,format=None):
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

        
    def delete(self,request,id,format=None):
        id=id
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'Data Deleted'}
        return Response(res)
    