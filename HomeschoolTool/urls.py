from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from HomeschoolTool.views.loginViews import loginView, createLogin, logoutReq
from HomeschoolTool.views.settingViews import settings
from HomeschoolTool.views.generalViews import view, home

urlpatterns = [
    path('', home),
    path('home', home, name=''),
    path('view', view),
    path('settings', settings, name='settings'),
    path('admin/', admin.site.urls),
    path('login/', loginView.as_view()),
    path('logout/', logoutReq),
    path('createLogin/', createLogin.as_view()),
]

