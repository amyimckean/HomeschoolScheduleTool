from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime
from HomeschoolTool.views.viewHelper import getEventSource
from HomeschoolTool.forms import scheduleItemForm
from HomeschoolTool.models import scheduledItem, subject, student, scheduleItemType, recurrenceType


def settings(request):
    subjects = subject.objects.all()
    scheduleItemTypes = scheduleItemType.objects.all()
    recurrenceTypes = recurrenceType.objects.all()
    students = student.objects.filter(parent=request.user)
    allEvents = scheduledItem.objects.all()
    form = scheduleItemForm()
    last = allEvents.order_by('scheduledItemID').last()
    id = 1 if last is None else last.scheduledItemID + 1
    if request.is_ajax and request.GET:
        id = request.GET.get('studentID')
        print(id)
        currentStudent = students.get(studentID=id)
        eventFiltered = allEvents.filter(student=currentStudent)
        data = {
            'eventSource': getEventSource(eventFiltered)
        }
        return JsonResponse(data)

    if request.method == "POST":
        postSubject(request)
        postStudent(request)
        postEvent(request, students, id)
    return render(request, "settings/settings.html", {"events": allEvents.filter(student=students.first().studentID),
                                                      "scheduleItemTypes": scheduleItemTypes,
                                                      "subjects": subjects,
                                                      "recurrenceTypes": recurrenceTypes,
                                                      "students": students,
                                                      "scheduleForm": form})


def getCurrentStudentID(request, students):
    res = 0
    if request.POST.get("selectStudent") is not None:
        res = request.POST.get("selectStudent")
    elif students.count() > 0:
        res = students.first().studentID
    return res


def postStudent(request):
    if request.POST.get('createStudentFirst') and request.POST.get('createStudentLast'):
        item = subject()
        studentLast = student.objects.all().order_by('studentID').last()
        id = studentLast.subjectID + 1
        item = {
            'studentID': id,
            'studentFirstName': request.POST.get("createStudentFirst"),
            'studentLastName': request.POST.get("createStudentLast")
        }
        student.objects.create(**item)


def postSubject(request):
    if request.POST.get('createSubject'):
        item = subject()
        subjectLast = subject.objects.all().order_by('subjectID').last()
        id = subjectLast.subjectID + 1
        item = {
            'subjectID': id,
            'subjectName': request.POST.get("createSubject")
        }
        subject.objects.create(**item)


def postEvent(request, students, id):
    if request.POST.get('selectStudent'):
        form = scheduleItemForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            item = form.save(commit=False)
            item.student = students.get(studentID=request.POST.get('selectStudent'))
            item.scheduledItemID =  id
            item.save()
