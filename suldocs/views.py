from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SuldocSerializer
from .models import Suldoc

# Create your views here.
class SuldocViewSet(viewsets.ModelViewSet):
    queryset = Suldoc.objects.all()
    serializer_class = SuldocSerializer
