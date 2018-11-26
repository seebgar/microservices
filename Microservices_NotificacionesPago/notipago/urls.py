from django.conf.urls import url, include

from .views import *

urlpatterns =[
    url(r'^notificaciones/$', notificaciones),
    url(r'^notificaciones/(?P<pk>\w+)/$', notificacionesDetail),

    url(r'^pagos/$', pagos),
    url(r'^pagos/(?P<pk>\w+)/$', pagosDetail),
]