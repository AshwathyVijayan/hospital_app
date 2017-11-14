from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^registration/$', views.RegisterUser.as_view()), 
    url(r'^home/$', views.HomePageView.as_view()), 
    url(r'^login/$', views.LoginUser.as_view()), 
]
