from django.shortcuts import render
from django.views.generic import TemplateView

from registrationmod.forms import *

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'home.html', context=None)


class RegisterUser(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'registration.html', context=None)

class LoginUser(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'login.html', context=None)

