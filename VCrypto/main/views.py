from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse('success')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Не найдено(</h1>')