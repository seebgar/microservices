from django.conf.urls import url, include

from .views import *

urlpatterns =[
    url(r'^oferentes/$', oferentes),
    url(r'^oferentes/(?P<pk>\w+)/$', oferentesDetail),
]