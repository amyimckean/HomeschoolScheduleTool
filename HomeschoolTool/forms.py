from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.admin import widgets
from django.utils.safestring import mark_safe
from django.forms import SplitDateTimeField, Textarea, RadioSelect
from django.forms.widgets import SplitDateTimeWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
import floppyforms.__future__ as forms
from datetime import datetime
from HomeschoolTool.models import *
from HomeschoolTool.fields import HorizontalRadioSelect, TeacherSelect


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        class Meta:
            model = User
            fields = ['username', 'email', 'first_name', 'last_name' 'password1', 'password2']


class classForm(forms.ModelForm):
    class Meta:
        model = teacherClass
        fields = ['className']
        labels = {
            'className': 'Class Name:'
        }

    def save(self, commit=True):
        model = super(classForm, self).save(commit=False)

        if commit:
            model.save()
        return model


class subjectForm(forms.ModelForm):
    class Meta:
        model = subject
        fields = '__all__'
        labels = {
            'subjectName': 'Subject:'
        }

    def save(self, commit=True):
        model = super(subjectForm, self).save(commit=False)

        if commit:
            model.save()
        return model


class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['firstName', 'lastName']
        labels = {
            'firstName': 'First Name:',
            'lastName': 'Last Name:',
        }

    def save(self, commit=True):
        model = super(studentForm, self).save(commit=False)

        if commit:
            model.save()
        return model


class scheduleItemForm(forms.ModelForm):
    subject = forms.ModelChoiceField(queryset=subject.objects.all(), to_field_name='subjectName')
    activity_date = forms.DateField()
    start_time = forms.TimeField(required=False)
    end_time = forms.TimeField(required=False)
    recurEnd = forms.DateField(required=False)
    teacher = TeacherSelect(queryset=User.objects.all(), to_field_name="id", required=False)

    class Meta:
        model = scheduledItem
        fields = ['description', 'subject', 'details', 'activity_date', 'start_time', 'end_time', 'type',
                  'recurEnd', 'recurType', 'teacher', 'classT']
        labels = {
            'description': 'Title:',
            'activity_date': 'Date:',
            'recurEnd': 'End Date:',
        }
        widgets = {
            'details': Textarea(attrs={'rows': 2, 'cols': 41}),
            'description': forms.TextInput(attrs={'size': '30'}),
            'type': HorizontalRadioSelect(choices=scheduleItemType.objects.all()),
            'recurType': HorizontalRadioSelect(choices=recurrenceType.objects.all()),
            'teacher':  forms.Select(attrs={'id': 'id'})
        }

    def __init__(self, *args, **kwargs):
        super(scheduleItemForm, self).__init__(*args, **kwargs)
        self.fields['recurEnd'].label = "Recurrence End:"
        self.fields['activity_date'].label = "Date:"
        self.fields['recurType'].label = "Frequency:"
        self.fields['classT'].label = "Class:"
        self.fields['recurType'].empty_label = None

    def save(self, commit=True):
        model = super(scheduleItemForm, self).save(commit=False)
        model.start = datetime.combine(self.cleaned_data['activity_date'], self.cleaned_data['start_time'])
        model.end = datetime.combine(self.cleaned_data['activity_date'], self.cleaned_data['end_time'])

        if commit:
            model.save()
        return model


