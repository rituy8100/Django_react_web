from django.shortcuts import render
from rest_framework import viewsets
from  .serializers import TestSerializer
from .models import Posts

class PostView(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Posts.objects.all()

