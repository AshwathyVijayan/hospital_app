from django.conf.urls import url, include
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
                       url(r'^register/$',views.Register),
                       url(r'^verify/$', views.verify_and_create),
]
                       

