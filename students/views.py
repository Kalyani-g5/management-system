from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Student
from .serializers import *

# Create your views here.
@api_view(['GET', 'POST'])
def students_list(request):
    if request.method == 'GET':
        data = Student.objects.all()

        serializers = StudentSerializer(data, context={'request': request}, many=True)

        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(status=status.HTTP_201_CREATED)
        
        return Response(serializers.errors, status=status.HTTP_400_BAD_Request)
    
@api_view(['PUT', 'DELETE'])
def student_detail(request, roll_no):
    try:
        student = Student.objects.get(roll_no=roll_no)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializers = StudentSerializer(student, data=request.data, context={"request": request})
        if serializers.is_valid():
            serializers.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)