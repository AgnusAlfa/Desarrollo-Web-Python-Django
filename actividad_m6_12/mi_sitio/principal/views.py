from django.shortcuts import render
from django.http import HttpResponse

def bienvenida(request):
    return HttpResponse("¡Bienvenido a mi sitio!")

