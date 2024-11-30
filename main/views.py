from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def zropage(request):
    text = "Salom bu mening brinchi DJANGO saytim"
    text += "<br><br>Asalomu alekum mening ismim Muhammadamin "
    return HttpResponse(text)