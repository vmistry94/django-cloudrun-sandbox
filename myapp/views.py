from django.shortcuts import render
from django.http import HttpResponse
from .models import Fruits

def homepage(request):
    fruits = Fruits.objects.all()
    context = {'fruits': fruits}
    return render(request, 'myapp/index.html', context)