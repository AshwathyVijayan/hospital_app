from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import HttpResponseRedirect
from django.contrib.auth import logout

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

class NewAppt(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'newappt.html', context=None)

def login(request):
    template = get_template('login.html')
    variables = Context({ 'user': request.user })
    output = template.render(variables)
    return HttpResponse(output)

