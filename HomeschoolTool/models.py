from django.db import models


class subject(models.Model):
    subjectID = models.AutoField(primary_key=True, default='')
    subjectName = models.CharField(max_length=50, default='')

    def __unicode__(self):
        return self.subjectName


class student(models.Model):
    studentID = models.AutoField(primary_key=True, default='')
    studentFirstName = models.CharField(max_length=50, default='')
    studentLastName = models.CharField(max_length=50, default='')

    def __unicode__(self):
        return self.studentFirstName + self.studentLastName


class week(models.Model):
    Time = models.TimeField()
    Monday = models.ForeignKey(subject, on_delete=models.CASCADE, related_name='Monday', null=True)
    Tuesday = models.ForeignKey(subject, on_delete=models.CASCADE, related_name='Tuesday', null=True)
    Wednesday = models.ForeignKey(subject, on_delete=models.CASCADE, related_name='Wednesday', null=True)
    Thursday = models.ForeignKey(subject, on_delete=models.CASCADE, related_name='Thursday', null=True)
    Friday = models.ForeignKey(subject, on_delete=models.CASCADE, related_name='Friday', null=True)
    Saturday = models.ForeignKey(subject, on_delete=models.CASCADE, related_name='Saturday', null=True)
    Sunday = models.ForeignKey(subject, on_delete=models.CASCADE, related_name='Sunday', null=True)
    StudentID = models.ForeignKey(student, on_delete=models.CASCADE, related_name='StudentID', null=True)

    def __unicode__(self):
        return self.Time
