from django.shortcuts import render

# Create your views here.
from .models import Blog


def home(request):
    return render(request, 'blogapp/home.html')


def blog(request):
    data = Blog.objects.all()

    return render(request, 'blogapp/blog.html', {'data': data})
