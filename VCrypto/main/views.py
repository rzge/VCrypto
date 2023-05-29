from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Не найдено(</h1>')