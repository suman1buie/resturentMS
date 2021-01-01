from django.shortcuts import render
from . models import Tables
import datetime


def home(request):
    return render(request, 'home.html', {})


def BookShit(request, id):
    table = Tables.objects.get(pk=id)
    table.is_booked = True
    crTime = datetime.datetime.now()
    table.started_timing = crTime
    table.save()
    return render(request, 'message.html', {})


def displayTable(request):
    allTables = Tables.objects.all()
    tables = []
    for table in allTables:
        if table.is_booked == False:
            tables.append(table)
    return render(request, 'index.html', {'tables': tables})
