from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})