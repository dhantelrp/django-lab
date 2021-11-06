from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Blog


def handler404(request):
    return render(request, '404.html', status=404)

def index(request):
    blogs = Blog.objects.all()
    # versi 2 jika halaman ada tak ditemukan
    # blogs = Blog.objects.all()
    # Versi 1. Menggunakan ini
    # output = ', '.join([str(blog) for blog in blogs])
    # return HttpResponse(output)
    # kemudian Versi 2 saat penambahan basic TEMPLATES
    return render(request, 'blogs/index.html', {'blogs': blogs})

def single(request, id):
    blog = get_object_or_404(Blog, pk=id)
    # blog = Blog.objects.get(pk = id)
    return render(request, 'blogs/single.html', {'blog': blog})


# Create your views here.
