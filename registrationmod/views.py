from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from registrationmod.forms import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'mysite/home.html', context=None)

class RegisterUser(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'registration.html', context=None)

class LoginUser(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'registration/login.html', context=None)

class NewAppt(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'newappt.html', context=None)

def home(request):
    return render(request, 'mysite/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')

    else:
        form = UserRegistrationForm()

    return render(request, 'mysite/register.html', {'form' : form})
