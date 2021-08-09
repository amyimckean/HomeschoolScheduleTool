from django.forms import RadioSelect, Select


class HorizontalRadioSelect(RadioSelect):
    template_name = 'settings/radioHorizontal.html'
    option_template_name = 'settings/inputOptionHorizontal.html'


class TeacherSelect(Select):
    def label_from_instance(self, obj):
        return "(" + obj.id + ") " + obj.first_name + " " + obj.last_name
