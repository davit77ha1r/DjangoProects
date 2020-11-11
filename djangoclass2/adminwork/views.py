from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
dict_1 = {
    "name": "Tigran",
    "last_name": "Danielyan",
}

def index(request):
    return render(request, "adminwork/welcome.html",dict_1)