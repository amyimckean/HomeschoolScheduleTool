from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime

from HomeschoolTool.models import scheduledItem, subject, student, scheduleItemType, recurrenceType


def settings(request):
    subjects = subject.objects.all()
    scheduleItemTypes = scheduleItemType.objects.all()
    recurrenceTypes = recurrenceType.objects.all()
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

    if request.method == "POST":
        postSubject(request)
        postStudent(request)
        postEvent(request, allEvents, subjects, scheduleItemTypes, recurrenceTypes, students)

    return render(request, "settings/settings.html", {"events": allEvents.filter(student=students.first().studentID),
                                                      "scheduleItemTypes": scheduleItemTypes,
                                                      "subjects": subjects,
                                                      "recurrenceTypes": recurrenceTypes,
                                                      "students": students})


def getEventSource(events):
    eventArr = []
    for e in events:
        event = {'title': e.description, 'description': e.details}
        start_date = e.start.strftime("%Y-%m-%d %H:%M:%S")
        event['start'] = start_date
        if e.end:
            end_date = e.end.strftime("%Y-%m-%d %H:%M:%S")
            event['end'] = end_date
        event['allDay'] = e.allDay
        if e.reoccurType:
            recurrStart = e.start.date().strftime("%Y%m%dT%H%M%S")
            recurrEnd = e.reoccurEnd.date().strftime("%Y%m%d")
            event['rrule'] = 'DTSTART:' + recurrStart + 'Z\nRRULE:FREQ=' + e.reoccurType.recurrenceTypeName \
                             + ';UNTIL=' + recurrEnd
        eventArr.append(event)
    return eventArr


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


def getRecurredDate(request):
    if request.POST.get("createEndRecurrenceDate"):
        current_tz = timezone.get_current_timezone()
        dateTime = datetime.strptime(request.POST.get("createEndRecurrenceDate") + "T12:00:00", '%Y-%m-%dT%H:%M:%S')
        return dateTime
    else:
        return None


def getRecurredType(request, recurrenceTypes):
    if request.POST.get("createEndRecurrenceDate"):
        return recurrenceTypes.get(recurrenceTypeID=request.POST.get("createEndRecurrenceType"))
    else:
        return None


def getDateTime(request, start, date, time):
    if request.POST.get("setAllDay") and not start:
        return None
    else:
        dateTime = datetime.strptime(date + "T" + time, "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
        return dateTimeselectedStudent


def postEvent(request, events, subjects, scheduleItemTypes, recurrenceTypes, students):
    if request.POST.get('selectStudent') and request.POST.get("createEvent") is not None:
        item = scheduledItem()
        last = events.order_by('scheduledItemID').last()
        id = 1 if last is None else last.scheduledItemID + 1
        item = {
            'scheduledItemID': id,
            'student': students.get(studentID=request.POST.get("selectStudent")),
            'subject': subjects.get(subjectID=request.POST.get("addSubject")),
            'type': scheduleItemTypes.get(scheduleItemTypeID=request.POST.get("addType")),
            'description': request.POST.get("createEvent"),
            'details': request.POST.get("createDetails"),
            'teacher': None,
            'allDay': True if request.POST.get("setAllDay") == "on" else False,
            'start': getDateTime(request, True, request.POST.get("createStartDate"),
                                 request.POST.get("createStartTime")),
            'end': getDateTime(request, False, request.POST.get("createStartDate"), request.POST.get("createEndTime")),
            'reoccurEnd': getRecurredDate(request),
            'reoccurType': getRecurredType(request, recurrenceTypes),
        }
        scheduledItem.objects.create(**item)
