from django.forms import RadioSelect, Select, ModelChoiceField


class HorizontalRadioSelect(RadioSelect):
    template_name = 'utilities/radioHorizontal.html'
    option_template_name = 'utilities/inputOptionHorizontal.html'


class TeacherSelect(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.first_name + " " + obj.last_name

