from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime
from HomeschoolTool.views.viewHelper import *
from HomeschoolTool.forms import *
from HomeschoolTool.models import *


def settings(request):
    students = student.objects.filter(parent=request.user) if any(student.objects.all()) else []
    if request.is_ajax and request.GET:
        if request.GET.get('studentID'):
            return JsonResponse(studentUpdate(request, students))
        if request.GET.get('teacher'):
            return JsonResponse(classUpdate(request))

    if request.method == "POST":
        postSubject(request)
        postStudent(request)
        postClass(request)
        postEvent(request, students)

    allEvents = []
    if len(students) > 0:
        allEvents = scheduledItem.objects.filter(student=students.first().id)

    status = request.session.get('status')
    request.session['status'] = ''
    return render(request, "settings/settings.html", {"events": allEvents,
                                                      "students": students,
                                                      "subjectForm": subjectForm(),
                                                      "subjects": subject.objects.all(),
                                                      "studentForm": studentForm(),
                                                      "classForm": classForm(),
                                                      "classes": teacherClass.objects.filter(teacher=request.user),
                                                      "status": status,
                                                      "scheduleForm": scheduleItemForm()})


def studentUpdate(request, students):
    currentStudent = students.get(id=request.GET.get('studentID'))
    eventFiltered = scheduledItem.objects.filter(student=currentStudent)
    data = {
        'eventSource': serializeEvents(eventFiltered)
    }
    return data


def classUpdate(request):
    classes = teacherClass.objects.filter(teacher=request.GET.get('teacher'))
    data = {
        'classes': serializeClasses(classes)
    }
    return data


def postClass(request):
    if request.POST.get('className'):
        form = classForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            item = form.save(commit=False)
            item.teacher = request.user
            item.save()
            request.session['status'] = "You have successfully saved a class!"


def postStudent(request):
    if request.POST.get('firstName'):
        form = studentForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            item = form.save(commit=False)
            item.parent = request.user
            item.save()
            request.session['status'] = "You have successfully created a student!"


def postSubject(request):
    if request.POST.get('subjectName'):
        form = subjectForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            form.save(commit=True)
            request.session['status'] = "You have successfully created a subject!"


def postEvent(request, students):
    if request.POST.get('selectStudent'):
        form = scheduleItemForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            item = form.save(commit=False)
            item.student = students.get(id=request.POST.get('selectStudent'))
            item.save()
            request.session['status'] = "  You have successfully scheduled your activity!"
