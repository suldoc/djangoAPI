from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SuldocSerializer
from .models import Taste_note
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

# Create your views here.
class SuldocViewSet(viewsets.ModelViewSet):
    queryset = Taste_note.objects.all()
    serializer_class = SuldocSerializer

def index(request):
    latest_note_list = Taste_note.objects.order_by('update_at')
    context = {'latest_note_list': latest_note_list}
    return render(request, 'notes/index.html', context)

def detail(request, note_id):
    note = get_object_or_404(Taste_note, pk=note_id)
    return render(request, 'notes/detail.html', {'note': note})