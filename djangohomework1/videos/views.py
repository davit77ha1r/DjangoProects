from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
month_dict = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August", 9:"September",10:"October", 11:"November", 12:"December"}

# Create your views here.

def index(request):
    return HttpResponse("<title>Main Page</title><body style=\"background-color:#F4CA16\"><h1>Hy welcome to our website :)</h1><h2>You can find here things to writing it after link or click on it</h2>  <br><a href=\"http://127.0.0.1:8000/greeting\">1.    /greeting</h3></a>   <br>   <a href=\"http://127.0.0.1:8000/introduction\">2.    /introduction</h3></a>   <br>   <a href=\"http://127.0.0.1:8000/datetime  \">3.    /datetime</h3></a>   <br>   <a href=\"http://127.0.0.1:8000/task\">4.    /task</h3></a></body>")
def greeting(request):
    return HttpResponse("<a href=\"http://127.0.0.1:8000/\">Back</a><title>Greeting</title><body style=\"background-color:#66FF99\"><h2>Hi my friend i think you will be happy to see my website wich i make with django. Thank you for visiting and i will be help you with everything GOOD TIME :) </h2><iframe width=\"742\" height=\"480\" src=\"https://www.youtube.com/embed/cpP-fCo8Dn4\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe></body>")
def introduction(request):
    return HttpResponse("<a href=\"http://127.0.0.1:8000/\">Back</a><title>Introduction</title><body style=\"background-color:#B120FF\"><h2>Hi i make this website in 2 or 3 hours Yes... It is simple.. but every first step is simple and than its can be so dificult... Now you can make a good time to walking in my website.There ara 5 URLS and you can click on tham or add word after link    Good Time :)</h2></body>")
def datetime1(request,datetime=datetime):
    now = datetime.now()
    todays_text = "<h1>Hi, You want to know todays date and time </h1> <br> 1.  Year is  {} <br>2. Today is {} of {} <br>3. Time is {}:{}:{} ,     microseconds are {}  (when you reload this site time will change)".format(now.year, now.day, month_dict[now.month], now.hour, now.minute, now.second, now.microsecond)
    return HttpResponse("<a href=\"http://127.0.0.1:8000/\">Back</a><title>Date and Time</title><body style=\"background-color:#00FF3C\"><h2>{}</h2></body>".format(todays_text))
def task(request):
    new_dict = {}
    return_text = 'Starting...<br>'
    for i in range(1, 16):
        new_dict[i] = i**2
        return_text += "The square of {} is {} <br> ".format(i,i**2)
    return_text += "Task ended successsfully <hr>Result dictionary:   {}".format(new_dict)
    return HttpResponse("<a href=\"http://127.0.0.1:8000/\">Back</a><title>Task</title><body style=\"background-color:#00D3D3\"><h3>{}</h3></body>".format(return_text))
