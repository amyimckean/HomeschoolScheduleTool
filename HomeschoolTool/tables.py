import django_tables2 as tables
from HomeschoolTool.models import week


class ScheduleTable(tables.Table):
    class Meta:
        model = week
        template_name = "django_tables2/bootstrap.html"
        fields = ("Time", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        attrs = {'class': 'paleblue'}

    def render_Monday(self, value):
        return value.subjectName

    def render_Tuesday(self, value):
        return value.subjectName

    def render_Wednesday(self, value):
        return value.subjectName

    def render_Thursday(self, value):
        return value.subjectName

    def render_Friday(self, value):
        return value.subjectName

    def render_Saturday(self, value):
        return value.subjectName

    def render_Sunday(self, value):
        return value.subjectName