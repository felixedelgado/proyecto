from re import template
from django.http import HttpResponse

from django.template import loader

from django.shortcuts import render

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

def about(request):
    return render(request, "about.html")