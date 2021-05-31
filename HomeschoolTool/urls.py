from django.conf.urls import include, url
from HomeschoolTool.views import index, schedule

urlpatterns = [
    url(r'^$', schedule, name='schedule'),
    url(r'^$', index, name='homepage'),
]

