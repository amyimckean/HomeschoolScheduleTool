from django.db import models
from django.contrib.auth.models import User


class subject(models.Model):
    subjectName = models.CharField(max_length=50, default='')

    def __str__(self):
        return '%s' % self.subjectName


class teacherClass(models.Model):
    className = models.CharField(max_length=50, default='')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '%s' % self.className


class student(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    firstName = models.CharField(max_length=50, default='')
    lastName = models.CharField(max_length=50, default='')

    def __str__(self):
        return '%s' % self.firstName + " " + self.lastName


class scheduleItemType(models.Model):
    ScheduleItemTypeName = models.CharField(max_length=50, default='')

    def __str__(self):
        return '%s' % self.ScheduleItemTypeName


class recurrenceType(models.Model):
    recurrenceTypeName = models.CharField(max_length=50, default='')

    def __str__(self):
        return '%s' % self.recurrenceTypeName


class scheduledItem(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE, default=0)
    type = models.ForeignKey(scheduleItemType, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, default='')
    details = models.CharField(max_length=255, default='', null=True, blank=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    classT = models.ForeignKey(teacherClass, on_delete=models.CASCADE, null=True, blank=True)
    start = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    end = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    allDay = models.BooleanField(default=True)
    recurEnd = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    recurType = models.ForeignKey(recurrenceType, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '%s' % self.subject.subjectName + " " + self.description


class completedItem(models.Model):
    item = models.ForeignKey(scheduledItem, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completedDate = models.DateTimeField(auto_now_add=False, blank=True)
