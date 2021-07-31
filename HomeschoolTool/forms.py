from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, Div, Submit, Row, Column, ButtonHolder, Submit, HTML


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


