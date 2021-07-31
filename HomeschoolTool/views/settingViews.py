from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic
from django.utils import timezone
from datetime import datetime

from HomeschoolTool.models import scheduledItem, subject, student, scheduleItemType, recurrenceType


def settings(request):
    events = scheduledItem.objects.all()
    subjects = subject.objects.all()
    scheduleItemTypes = scheduleItemType.objects.all()
    recurrenceTypes = recurrenceType.objects.all()
    students = student.objects.all()
    if request.method == "POST":
        postSubject(request)
        postStudent(request)
        postEvent(request, events, subjects, scheduleItemTypes, recurrenceTypes, students)

    recurringEvents = []
    nonrecurringEvents = []
    for event in events:
        if event.reoccurType:
            recurringEvents.append(event)
        else:
            nonrecurringEvents.append(event)

    return render(request, "settings/settings.html", {"recurringEvents": recurringEvents,
                                                      "nonrecurringEvents": nonrecurringEvents,
                                                      "scheduleItemTypes": scheduleItemTypes,
                                                      "subjects": subjects,
                                                      "recurrenceTypes": recurrenceTypes,
                                                      "students": students})


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
        dateTime = current_tz.localize(datetime.strptime(request.POST.get("createEndRecurrenceDate")
                                                         + " 12:00:00", '%Y-%m-%d %H:%M:%S'))
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
        return dateTime


def postEvent(request, events, subjects, scheduleItemTypes, recurrenceTypes, students):
    if request.POST.get('selectStudent'):
        item = scheduledItem()
        last = events.order_by('scheduledItemID').last()
        id = 1 if last is None else last.scheduledItemID + 1
        print(getDateTime(request, True, request.POST.get("createStartDate"), request.POST.get("createStartTime")))
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
