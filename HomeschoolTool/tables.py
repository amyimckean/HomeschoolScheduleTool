import django_tables2 as tables
from HomeschoolTool.models import scheduledItem


class ScheduleTable(tables.Table):
    Monday = tables.Column()
    Tuesday = tables.Column()
    Wednesday = tables.Column()
    Thursday = tables.Column()
    Friday = tables.Column()
    Saturday = tables.Column()
    Sunday = tables.Column()


    class Meta:
        template_name = "django_tables2/bootstrap.html"
        fields = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        model = scheduledItem
        attrs = {'class': 'paleblue'}

    def render_Monday(self, value, record):
        if record.day.name == "Monday":
            return record.subject.subjectName

    def render_Tuesday(self, value, record):
        if record.day.name == "Tuesday":
            return record.subject.subjectName

    def render_Wednesday(self, value, record):
        if record.day.name == "Wednesday":
            return record.subject.subjectName

    def render_Thursday(self, value, record):
        if record.day.name == "Thursday":
            return record.subject.subjectName

    def render_Friday(self, value, record):
        if record.day.name == "Friday":
            return record.subject.subjectName

    def render_Saturday(self, value, record):
        if record.day.name == "Saturday":
            return record.subject.subjectName

    def render_Sunday(self, value, record):
        if record.day.name == "Sunday":
            return record.subject.subjectName
