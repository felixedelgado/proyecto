from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from calendar import HTMLCalendar, Calendar
from django.contrib import messages
import datetime
from datetime import date
from .form import EventForm, EventForm1
from email import message
import calendar
from django.contrib.auth.decorators import login_required
# Create your views here.

# def calendario(request):
#     now = datetime.datetime.now()
#     nowd = now.day
#     nowm = now.month
#     nowy = now.year
#     cal = calendar.LocaleHTMLCalendar().formatmonth(nowy, nowm)
#     return render(request, 'calendario/calendar.html', {'cal': cal})


def calendario(request, m):
    event = Event.objects.all()
    now = datetime.datetime.now()
    nowd = now.day
    nowm = now.month
    nowy = now.year
    # mes = now.strftime("%B")
    mes = f"{nowm}"
    mesesDic = {
        "1":'Enero',
        "2":'Febrero',
        "3":'Marzo',
        "4":'Abril',
        "5":'Mayo',
        "6":'Junio',
        "7":'Julio',
        "8":'Agosto',
        "9":'Septiembre',
        "10":'Octubre',
        "11":'Noviembre',
        "12":'Diciembre',
    }
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    mes = mesesDic[mes]
    mesesnum = {
        'Enero': 1,
        'Febrero': 2,
        'Marzo': 3,
        'Abril': 4,
        'Mayo' : 5,
        'Junio': 6,
        'Julio': 7,
        'Agosto': 8,
        'Septiembre': 9,
        'Octubre': 10,
        'Noviembre': 11,
        'Diciembre': 12,
    }
    mesnum = mesesnum[m]
    if mesnum == nowm:
        cal= calendar.Calendar()
        cal = cal.monthdayscalendar(nowy, nowm)
    else:
        cal= calendar.Calendar()
        cal = cal.monthdayscalendar(nowy, mesnum)
        mes = m
    return render(request, 'calendario/calendar.html', {'event':event,'cal': cal, 'mes': mes, 'month': mesnum,'day': nowd, 'year': nowy, 'meses': meses, 'month1': nowm})

def calendario_base(request):
    event = Event.objects.all()
    now = datetime.datetime.now()
    nowd = now.day
    nowm = now.month
    nowy = now.year
    # mes = now.strftime("%B")
    mes = f"{nowm}"
    mesesDic = {
        "1":'Enero',
        "2":'Febrero',
        "3":'Marzo',
        "4":'Abril',
        "5":'Mayo',
        "6":'Junio',
        "7":'Julio',
        "8":'Agosto',
        "9":'Septiembre',
        "10":'Octubre',
        "11":'Noviembre',
        "12":'Diciembre',
    }
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    mes = mesesDic[mes]
    cal= calendar.Calendar()
    cal = cal.monthdayscalendar(nowy, nowm)
    return render(request, 'calendario/calendario_base.html', {'event':event, 'cal': cal, 'mes': mes, 'month': nowm,'day': nowd, 'year': nowy, 'meses': meses})

@login_required
def event_create(request, year, month, d):
    if not request.user.is_admin:
        return redirect('index')
    fecha = datetime.date(year, month, d)
    fecha = fecha.strftime("%Y-%m-%d")
    form = EventForm1()
    if request.method == 'POST':
        form = EventForm1(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.date = fecha
            # fecha = f'{d}/{month}/{year}'
            event.save()
            messages.success(request, 'Evento guardado con exito')
            return redirect('calendario_base')
        messages.error(request, 'Hay errores en el formulario')
    form = EventForm1()
    return render(request, 'calendario/eventos.html', {'form': form, 'fecha': fecha })


@login_required
def event_delete(request, pk):
    if not request.user.is_admin:
        return redirect('index')
    event = get_object_or_404(Event, id=pk)
    event.delete()
    return redirect('event_view')

def event_view(request):
    event = Event.objects.all()
    return render(request, 'calendario/event_view.html', {'event': event})

@login_required
def event_update(request, pk):
    if not request.user.is_admin:
        return redirect('index')
    event = get_object_or_404(Event, id=pk)
    data = event
    data.date = data.date.strftime("%Y-%m-%d")
    form = EventForm(initial={'name':data.name, 'date':data.date, 'hora':data.hora, 'lugar':data.lugar, 'descripcion':data.descripcion})
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_view')
    return render(request, 'calendario/event_update.html', {'form': form, 'event': event, 'data': data})

@login_required
def event_create_date(request):
    if not request.user.is_admin:
        return redirect('index')
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento guardado con exito')
            return redirect('event_view')
        messages.error(request, 'Hay errores en el formulario')
    form = EventForm()
    return render(request, 'calendario/eventos_nuevo.html', { 'form': form })