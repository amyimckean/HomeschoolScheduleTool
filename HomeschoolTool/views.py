from django.shortcuts import render
from django.views.generic import ListView

from HomeschoolTool.models import week, subject
from HomeschoolTool.tables import ScheduleTable
from django.contrib import messages


def schedule(request):
    table = ScheduleTable(week.objects.all())
    return render(request, "HomeschoolTool/schedule.html", {
        "table": table
    })


def settings(request):
    return render(request, "HomeschoolTool/settings.html")


def addSubject(request):
    if request.method == "POST":
        item = subject()
        subjectLast = subject.objects.all().order_by('subjectID').last()
        id = subjectLast.subjectID + 1
        item = {
            'subjectID': id,
            'subjectName': request.POST.get("addSubject")
        }
        subject.objects.create(**item)
    return render(request, "HomeschoolTool/settings.html")


def home(request):
    return render(request, "HomeschoolTool/home.html")
