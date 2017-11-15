from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from registrationmod.forms import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms



class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'mysite/home.html', context=None)

class RegisterUser(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'registration.html', context=None)

class LoginUser(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index/login.html', context=None)

class NewAppt(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'newappt.html', context=None)

def home(request):
    return render(request, 'mysite/home.html')

def login(request):
    return render(request, 'index/login.html')

def loginprocess(request):
	username =  request.POST.get("username","")
	password = request.POST.get("password","")
	if(len(username) ==0  and len(password) == 0):
		return render(request,'index/login.html',{'loginmessage' : 'Enter valid Name and password'  })
	user_data = User.objects.all().filter(username = username)
	got = True
	for e in user_data:
		got = False
	if(got):
		return render(request,'index/login.html',{'loginmessage' : 'Profile Does Not Exist Please Register '})

	for e in user_data:
		if(e.password != password):
			return render(request,'index/login.html',{'loginmessage' : 'Password/User Name entered is wrong please Try again' })

	request.session['logid'] = patientid
	return HttpResponseRedirect('mysite/home')
