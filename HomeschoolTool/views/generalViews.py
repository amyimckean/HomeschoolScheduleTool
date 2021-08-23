from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic
from django.http import JsonResponse
from django.core import serializers
from HomeschoolTool.views.viewHelper import *
from HomeschoolTool.models import *
from django.template.loader import render_to_string


def view(request):
    if request.is_ajax and request.GET:
        if request.GET.get('studentID'):
            return JsonResponse(studentUpdate(request))
        if request.GET.get('teacherStudentID'):
            return JsonResponse(teacherStudentUpdate(request))
        if request.GET.get('class'):
            classStudents = getStudentClasses(request.GET.get('class'))
            context = {
                "classStudents": classStudents
            }
            return render(request, 'studentTableBody.html', context)

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

    classes = teacherClass.objects.filter(teacher=request.user)

    classStudents = []
    if len(classes) > 0:
        classStudents = getStudentClasses(classes.first().id)

    return render(request, "view.html", {
        "events": allEvents,
        "students": students,
        "teacherStudents": teacherStudents,
        "teacherEvents": teacherEvents,
        "classes": classes,
        "classStudents": classStudents
    })


def studentUpdate(request):
    currentStudent = student.objects.get(id=request.GET.get('studentID'))
    eventFiltered = scheduledItem.objects.filter(student=currentStudent)
    data = {
        'eventSource': serializeEvents(eventFiltered)
    }
    return data


def teacherStudentUpdate(request):
    currentStudent = student.objects.get(id=request.GET.get('teacherStudentID'))
    eventFiltered = scheduledItem.objects.filter(student=currentStudent, teacher=request.user)
    data = {
        'eventSource': serializeEvents(eventFiltered)
    }
    return data


def getStudentClasses(classID):
    classStudents = []
    classItems = scheduledItem.objects.filter(classT=classID)
    classStudentByItem = classItems.values('student').order_by().values_list('student', flat=True).distinct()
    for s in classStudentByItem:
        stud = student.objects.get(id=s)
        classStudent = {'student': {'firstName': stud.firstName, 'lastName': stud.lastName},
                        'classes': serializeScheduledItems(scheduledItem.objects.filter(classT=classID, student=s))}
        classStudents.append(classStudent)
    return classStudents


def viewUpdate(request):
    request.session['view'] = request.GET.get('view')


def home(request):
    status = request.session.get('status')
    request.session['status'] = ""
    return render(request, "home.html", {"status": status, })
