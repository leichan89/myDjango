from django.shortcuts import render
from django.http import HttpResponse


def myindex(request):
    return HttpResponse("hello")
