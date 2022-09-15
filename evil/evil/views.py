from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def index1(request):
    return render(request, 'main/index1.html')

def index2(request):
    return render(request, 'main/index2.html')