from django.http import HttpResponse

def hello_bosku(request):
    return HttpResponse("hello bosku!!!")
