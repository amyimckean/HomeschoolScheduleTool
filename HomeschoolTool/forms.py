from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.admin import widgets
from django.utils.safestring import mark_safe
from django.forms import SplitDateTimeField, Textarea, RadioSelect
from django.forms.widgets import SplitDateTimeWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, Div, Submit, Row, Column, ButtonHolder, Submit, HTML
import floppyforms.__future__ as forms
from datetime import datetime
from HomeschoolTool.models import scheduledItem, subject, student, scheduleItemType, recurrenceType
from HomeschoolTool.fields import HorizontalRadioSelect, TeacherSelect


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div('username', id="username-field", css_class="hsField"),
            Div('password', id="password-field", css_class="hsField"),
            ButtonHolder(
                Submit('login', 'Login', css_class='hsButton'),
            ),
            ButtonHolder(
                HTML('<a href="../createLogin" class="hsButton">Create New User</a>')
            )
        )


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div('username', id="username-field", css_class="hsField"),
            Div('email', id="email-field", css_class="hsField"),
            Div('password1', id="password-field", css_class="hsField"),
            Div('password2', id="raw_password-field", css_class="hsField"),
            ButtonHolder(
                Submit('Submit', 'Login', css_class='hsButton')
            )
        )


class scheduleItemForm(forms.ModelForm):
    subject = forms.ModelChoiceField(queryset=subject.objects.all(),
                                     to_field_name='subjectName')
    activity_date = forms.DateField()
    start_time = forms.TimeField(required=False)
    end_time = forms.TimeField(required=False)
    recurEnd = forms.DateField(required=False)

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
            'details': Textarea(attrs={'rows': 2, 'cols': 48}),
            'description': forms.TextInput(attrs={'size': '35'}),
            'type': HorizontalRadioSelect(choices=scheduleItemType.objects.all()),
            'recurType': HorizontalRadioSelect(choices=recurrenceType.objects.all()),
            'teacher': TeacherSelect(),
        }

    def __init__(self, *args, **kwargs):
        super(scheduleItemForm, self).__init__(*args, **kwargs)
        self.fields['recurEnd'].label = "Recurrence End:"
        self.fields['activity_date'].label = "Date:"
        self.fields['recurType'].label = "Frequency:"
        self.fields['classT'].label = "Class:"

    def save(self, commit=True):
        model = super(scheduleItemForm, self).save(commit=False)
        model.start = datetime.combine(self.cleaned_data['activity_date'], self.cleaned_data['start_time'])
        model.end = datetime.combine(self.cleaned_data['activity_date'], self.cleaned_data['end_time'])

        if commit:
            model.save()

        return model

