from django.shortcuts import render
from django.http import HttpResponse

import json
import os
import random


# Create your views here.


def index(request):
    return render(request, 'main/main.html')
def json_read(request):
    with open('{}\main\other\main.json'.format(os.getcwd()), 'r') as file:
        json_text = json.load(file)
    text_starting = "Dictionary is -----{}".format(json_text)
    main_html = '''
    <title>Json make readable</title>
    <body style=\"background-color:#B179F1\">
        <a href= \"http://127.0.0.1:8000/\" style=\"color:#512089\">Back</a>
        <h1 style=\"color:#512089\">Json to Readable</h1>
        <h3  style=\"color:#512089\">Program succassfully finished reading json file</h3>
        <h3  style=\"color:#512089\">{}</h3>
    <body>
    '''.format(text_starting)
    return HttpResponse(main_html)
def check(request):
    return render(request, 'main/check.html')
def task(request):
    list_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
    list_values = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    dict_1 = {}
    dict_2 = {}
    result_dict = {}
    i = 0
    while i < 10:
        key = random.choice(list_keys)
        if (key in dict_1) is False:
            dict_1[key] = random.choice(list_values)
            i += 1
    i = 0
    while i < 10:
        key = random.choice(list_keys)
        if (key in dict_2) is False:
            dict_2[key] = random.choice(list_values)
            i += 1

    for key in dict_1:
        if key in result_dict:
            result_dict[key] += dict_1[key]
        else:
            result_dict[key] = dict_1[key]
    for key in dict_2:
        if key in result_dict:
            result_dict[key] += dict_2[key]
        else:
            result_dict[key] = dict_2[key]

    main_html = '''
    <title>Task with dictionaries</title>
    <body style=\"background-color:#484848\">
        <a href= \"http://127.0.0.1:8000/\" style=\"color:#FF9800\">Back</a>
        <h1 style=\"color:#FF9800\">This is task answer</h1>
        <h3  style=\"color:#FF9800\">This is first dictionary: {}</h3>
        <h3  style=\"color:#FF9800\">This is second dictionary: {}</h3>
        <h3  style=\"color:#FF9800\">This is mix of dictionaries: {}</h3>
        <br> <a href= \"http://127.0.0.1:8000/task\" style=\"color:#FF9800\">Click for changing values or refresh</a>
<body>
    '''.format(dict_1, dict_2, result_dict)

    return HttpResponse(main_html)


