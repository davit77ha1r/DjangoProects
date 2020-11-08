from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return HttpResponse("Hello django world")
def last_name(request):
	return HttpResponse("I am Davide  Harutyunyan")
def ok(request):
	return HttpResponse("(XXXXX)")