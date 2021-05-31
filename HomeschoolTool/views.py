from django.shortcuts import render
from django.views.generic import ListView

from HomeschoolTool.models import schedule
from HomeschoolTool.tables import ScheduleTable


def index(request):
    context = {
        "daysOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    }
    return render(request, "HomeschoolTool/index.html", context)


def schedule(request):
    table = ScheduleTable(schedule.objects.all())
    return render(request, "HomeschoolTool/schedule.html", {
        "table": table
    })

