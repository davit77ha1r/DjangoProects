from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h3>Hello World<h3>")
def about(request):
    return HttpResponse("<h1>Hy in this page you will see many iteresting</h4>")
def html(request):
    return render(request, 'main/index.html')