from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic
from django.http import JsonResponse
from HomeschoolTool.views.viewHelper import getEventSource
from HomeschoolTool.models import scheduledItem, subject, student, scheduleItemType, recurrenceType


def view(request):
    students = student.objects.filter(parent=request.user)
    allEvents = scheduledItem.objects.all()
    if request.is_ajax and request.GET:
        if request.GET.get('view'):
            request.session['view'] = request.GET.get('view')

            if request.session['view'] == 'teacher':
                students = student.objects.filter(teacher=request.user)

            if request.session['view'] == 'parent':
                students = student.objects.filter(parent=request.user)

        if request.GET.get('studentID'):
            id = request.GET.get('studentID')
            currentStudent = students.get(studentID=id)
            eventFiltered = allEvents.filter(student=currentStudent)
        data = {
            'eventSource': getEventSource(eventFiltered) if eventFiltered else None
        }
        return JsonResponse(data)
    return render(request, "view.html", {"events": allEvents.filter(student=students.first().studentID), "students": students})


def home(request):
    status = request.session.get('status')
    request.session['status'] = ""
    return render(request, "home.html", {"status": status, })
