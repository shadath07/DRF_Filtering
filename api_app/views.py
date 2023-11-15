from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView


# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby = user)
