from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    # return HttpResponse("hello bosku!!!")
    return render(request, 'welcome.html')
