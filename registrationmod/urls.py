from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^registration/$', views.RegisterUser.as_view()), 
    url(r'^registration/home/$', views.HomePageView.as_view()), 

]
