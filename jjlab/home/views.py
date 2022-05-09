from django.shortcuts import render
from rest_framework import viewsets
from  .serializers import TestSerializer
from .models import Test

class TestView(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()


def test1(request):
    query=Test.objects.get(pk=1)
    context= {'testText':query}
    return render(request,'home/test.html',context)

# Create your views here.
