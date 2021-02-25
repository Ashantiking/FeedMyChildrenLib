from django.shortcuts import render
from django.views.generic import ListView, DetailView


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def blog1(request):
    return render(request, 'blog1.html', {})