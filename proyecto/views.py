from re import template
from django.http import HttpResponse

from django.template import loader

from django.shortcuts import render

import datetime

# def saludo(request, horas):
#     now = datetime.datetime.now()
#     hora = now +datetime.timedelta(hours=horas)
#     template = loader.get_template("saludo.html")
#     context ={
#         'hora': now,
#         'adelantado' : hora,
#         'valor' : horas
#     }
#     return HttpResponse(template.render(context, request))

def saludo(request, horas):
    now = datetime.datetime.now()
    hora = now +datetime.timedelta(hours=horas)
    context ={
        'hora': now,
        'adelantado' : hora,
        'valor' : horas
    }
    return render(request, "saludo.html", context)