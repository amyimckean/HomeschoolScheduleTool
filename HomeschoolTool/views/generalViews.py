from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic

from HomeschoolTool.models import scheduledItem, subject, student, scheduleItemType, recurrenceType


def view(request):
    events = scheduledItem.objects.all()
    recurringEvents = []
    nonrecurringEvents = []
    for event in events:
        if event.reoccurType:
            recurringEvents.append(event)
        else:
            nonrecurringEvents.append(event)
    table = ScheduleTable(scheduledItem.objects.all())
    return render(request, "view.html", {
        "table": table,
        "recurringEvents": recurringEvents,
        "nonrecurringEvents": nonrecurringEvents,
    })


def home(request):
    return render(request, "home.html")


