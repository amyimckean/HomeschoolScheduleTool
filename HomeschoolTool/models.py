from django.db import models
from django.contrib.auth.models import User


class subject(models.Model):
    subjectID = models.AutoField(primary_key=True, default='')
    subjectName = models.CharField(max_length=50, default='')

    def __str__(self):
        return '%s' % self.subjectName


class teacherClass(models.Model):
    classID = models.AutoField(primary_key=True, default='')
    className = models.CharField(max_length=50, default='')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '%s' % self.className


class student(models.Model):
    studentID = models.AutoField(primary_key=True, default='')
    parent = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    studentFirstName = models.CharField(max_length=50, default='')
    studentLastName = models.CharField(max_length=50, default='')

    def __str__(self):
        return '%s' % self.studentFirstName + " " + self.studentLastName


class scheduleItemType(models.Model):
    scheduleItemTypeID = models.AutoField(primary_key=True, default='')
    ScheduleItemTypeName = models.CharField(max_length=50, default='')

    def __str__(self):
        return '%s' % self.ScheduleItemTypeName


class recurrenceType(models.Model):
    recurrenceTypeID = models.AutoField(primary_key=True, default='')
    recurrenceTypeName = models.CharField(max_length=50, default='')

    def __str__(self):
        return '%s' % self.recurrenceTypeName


class scheduledItem(models.Model):
    scheduledItemID = models.AutoField(primary_key=True, default=1)
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


