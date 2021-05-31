from django.db import models
from HomeschoolTool.Enums import Subject


class schedule(models.Model):
    Monday: models.CharField(choices=[(tag, tag.value) for tag in Subject])
    Tuesday: models.CharField(choices=[(tag, tag.value) for tag in Subject])
    Wednesday: models.CharField(choices=[(tag, tag.value) for tag in Subject])
    Thursday: models.CharField(choices=[(tag, tag.value) for tag in Subject])
    Friday: models.CharField(choices=[(tag, tag.value) for tag in Subject])
    Saturday: models.CharField(choices=[(tag, tag.value) for tag in Subject])
    Sunday: models.CharField(choices=[(tag, tag.value) for tag in Subject])
