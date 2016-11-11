from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from random import randrange
from auth.models import *
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from auth.forms import *
from django.contrib.auth import logout

class LoginView(FormView):
    template_name = "register/login.html"
    form_class = LoginForm

    def get_success_url(self):
        return '/accounts/login'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        success_url = self.get_success_url()
        return form.login(self.request, redirect_url = success_url)

login = LoginView.as_view()
def logout_auth(request):
    logout(request)
    return redirect('/')
