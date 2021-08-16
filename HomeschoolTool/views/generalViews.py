from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic
from django.http import JsonResponse
from django.core import serializers
from HomeschoolTool.views.viewHelper import *
from HomeschoolTool.models import *


def view(request):
    if request.is_ajax and request.GET:
        if request.GET.get('studentID'):
            return JsonResponse(studentUpdate(request))

    teacherStudents = []
    teacherEvents = []
    allEventsWithTeacher = scheduledItem.objects.filter(teacher=request.user)
    studentEvents = allEventsWithTeacher.filter(teacher=request.user).values_list('student', flat=True).distinct()
    for s in studentEvents:
        teacherStudents.append(student.objects.get(id=s))
    if len(teacherStudents) > 0:
        teacherEvents = scheduledItem.objects.filter(student=teacherStudents[0].id, teacher=request.user)

    students = student.objects.filter(parent=request.user) if any(student.objects.all()) else []
    allEvents = []
    if len(students) > 0:
        allEvents = scheduledItem.objects.filter(student=students.first().id)

    return render(request, "view.html", {
        "events": allEvents,
        "students": students,
        "teacherStudents": teacherStudents,
        "teacherEvents": teacherEvents
    })


def studentUpdate(request):
    currentStudent = student.objects.get(id=request.GET.get('studentID'))
    eventFiltered = scheduledItem.objects.filter(student=currentStudent)
    data = {
        'eventSource': serializeEvents(eventFiltered)
    }
    return data


def viewUpdate(request):
    request.session['view'] = request.GET.get('view')


def home(request):
    status = request.session.get('status')
    request.session['status'] = ""
    return render(request, "home.html", {"status": status, })
