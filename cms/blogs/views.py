from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello Bos ada di /Blog!!!')

# Create your views here.
