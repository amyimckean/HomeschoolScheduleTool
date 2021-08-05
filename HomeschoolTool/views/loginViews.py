from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib import messages

from HomeschoolTool.forms import LoginForm, CreateUserForm


class createLogin(generic.FormView):
    form_class = CreateUserForm
    success_url = reverse_lazy('')
    template_name = 'login/createLogin.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(createLogin, self).form_valid(form)
        else:
            return self.form_invalid(form)


class loginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('')
    template_name = 'login/loginView.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            self.request.session['status'] = "  You are now logged in as " + username + "."
            return super(loginView, self).form_valid(form)
        else:
            return self.form_invalid(form)

def logoutReq(request):
    logout(request)
    status = "You are now logged out."
    return render(request, "home.html", {"status": status, })