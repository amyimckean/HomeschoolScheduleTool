from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from HomeschoolTool.views import settings, schedule, home, addSubject

urlpatterns = [
    path('', home),
    path('home', home),
    path('schedule', schedule),
    path('settings', settings),
    path('addSubject', addSubject),
    path('admin/', admin.site.urls),
]

