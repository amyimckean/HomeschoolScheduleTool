from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic
from HomeschoolTool.models import scheduledItem, subject, student, scheduleItemType, recurrenceType


def view(request):
    students = student.objects.filter(parent=request.user)
    allEvents = scheduledItem.objects.all()
    if request.is_ajax and request.GET:
        id = request.GET.get('id')
        currentStudent = students.get(studentID=id)
        eventFiltered = allEvents.filter(student=currentStudent)
        data = {
            'eventSource': getEventSource(eventFiltered)
        }
        return JsonResponse(data)
    return render(request, "view.html", {"events": allEvents.filter(student=students.first().studentID), "students": students})


def home(request):
    status = request.session.get('status')
    request.session['status'] = ""
    return render(request, "home.html", {"status": status, })
