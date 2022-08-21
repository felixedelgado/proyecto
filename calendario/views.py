from django.shortcuts import render, redirect
from .models import Event
from calendar import HTMLCalendar, Calendar
from django.contrib import messages
import datetime
from .form import EventForm
from email import message
import calendar
# Create your views here.

# def calendario(request):
#     now = datetime.datetime.now()
#     nowd = now.day
#     nowm = now.month
#     nowy = now.year
#     cal = calendar.LocaleHTMLCalendar().formatmonth(nowy, nowm)
#     return render(request, 'calendario/calendar.html', {'cal': cal})


def calendario(request):
    now = datetime.datetime.now()
    nowd = now.day
    nowm = now.month
    mes = now.strftime("%B")
    nowy = now.year
    cal= calendar.Calendar()
    cal = cal.monthdayscalendar(nowy, nowm)
    return render(request, 'calendario/calendar.html', {'cal': cal, 'mes': mes, 'month': nowm, 'year': nowy})

def event_create(request, year, month, d):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            fecha = f'{d}/{month}/{year}'
            event.date = datetime.datetime.strptime(fecha, '%d/%m/%Y')
            event.save()
            messages.success(request, 'Post guardado con exito')
            return redirect('calendario')
        messages.error(request, 'Hay errores en el Post')
    form = EventForm()
    return render(request, 'calendario/eventos.html', {'form': form})

# def calendario(request):
#     now = datetime.datetime.now()
#     nowd = now.day
#     nowm = now.month
#     nowy = now.year
#     tc= calendar.TextCalendar(firstweekday=0)
#     cal = tc.formatmonth(nowy, nowm)
#     return render(request, 'calendario/calendar.html', {'cal': cal})

