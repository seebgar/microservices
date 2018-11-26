from django.conf.urls import url, include

from .views import *

urlpatterns =[
    url(r'^reservas/$', reservas),
    url(r'^reservas/(?P<pk>\w+)/$', reservasDetail),
]