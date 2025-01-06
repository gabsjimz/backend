from django.shortcuts import render
from django.http import HttpResponse
#solicitudes http
# Create your views here.
def index(request): #función
    #return HttpResponse("Hello, World!")
    #return render(request, 'main/base.html')
    return render(request, 'main/index.html')