from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def amma(request):
    return HttpResponse("<h1><marquee>' Hi amma how r u'<h1><marquee>")
