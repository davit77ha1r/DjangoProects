from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Message
from django.http import HttpResponse



# Create your views here.

def home(request):
    return render(request, "model_app/main.html")

def messages(request):
    messages = Message.objects.all()
    users = User.objects.all()
    context = {}
    a = 0
    for i in messages:
        a += 1
        new_dixt = {}
        new_dixt['Message'] = i[1]
        context[a] = i
    print(context, "ooooooooooooooooooooooooooooooo")


    return render(request, 'model_app/messages.html',context)