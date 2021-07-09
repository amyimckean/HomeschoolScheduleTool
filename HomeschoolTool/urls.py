from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from HomeschoolTool.views import settings, view, home

urlpatterns = [
    path('', home),
    path('home', home),
    path('view', view),
    path('settings', settings),
    path('admin', admin.site.urls),
    url(r'^schedule/', include('schedule.urls')),
]

