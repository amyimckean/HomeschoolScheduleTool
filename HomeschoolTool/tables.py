import django_tables2 as tables

from HomeschoolTool.Enums import Subject
from HomeschoolTool.models import schedule


class ScheduleTable(tables.Table):
    class Meta:
        model = schedule
        template_name = "django_tables2/bootstrap.html"
        fields = ("Time", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        attrs = {'class': 'paleblue'}
