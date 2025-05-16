from django.shortcuts import render
from .models import Nodes

# Create your views here.

def home(request):
    nodes = Nodes.objects.all()
    return render(request, 'node_manager/home.html', {"nodes": nodes})