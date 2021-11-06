from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def index(request):
    blogs = Blog.objects.all()
    # Versi 1. Menggunakan ini
    # output = ', '.join([str(blog) for blog in blogs])
    # return HttpResponse(output)
    # kemudian Versi 2 saat penambahan basic TEMPLATES
    return render(request, 'blogs/index.html', {'blogs': blogs})

def single(request, id):
    blog = Blog.objects.get(pk = id)
    return render(request, 'blogs/single.html', {'blog': blog})


# Create your views here.
