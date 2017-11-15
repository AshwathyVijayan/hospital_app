from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.LoginUser.as_view()),
    url(r'^login/$', views.LoginUser.as_view()),
    url(r'^registration/$', views.RegisterUser.as_view()), 
    url(r'^home/$', views.HomePageView.as_view()), 
    url(r'^login/newappt$', views.NewAppt.as_view()),
   

   
]
