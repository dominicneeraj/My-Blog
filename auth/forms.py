from django import forms
from django.contrib.auth.models import User as User
from django.db import transaction
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm
from django.contrib.auth import authenticate, login 
from django.utils import timezone

from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.http.response import HttpResponseRedirect, HttpResponse

class LoginForm(forms.Form):
    username = forms.CharField(label = _("Username"), required = True)
    password = forms.CharField(label = _('Password'), required = True, widget = forms.PasswordInput)
#    remember = forms.BooleanField(label = _("Remember Me"), required = False)
    user = None
    
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if self.is_valid():
            user = authenticate(username = self.cleaned_data['username'], password = self.cleaned_data['password'])
            if user:
                if user.is_active:
                    self.user = user
                else:
                    raise forms.ValidationError(_("This account is currently inactive"))
            else:
                raise forms.ValidationError(_('Incorrect credentials provided'))
            return self.cleaned_data
        raise forms.ValidationError(_("All fields are mandatory"))
    
    def get_success_url(self):
        return '/'
    
    def get_fail_url(self):
        return '/accounts/login'
    
    def login(self, request, redirect_url = None):
        user = self.user
        if user is not None:
            if user.is_active:
                login(request, user)
                ret = self.get_success_url() 
            else:
                ret = self.get_fail_url()
        else:
            ret = self.get_fail_url()
        request.session.set_expiry(60 * 60 * 24 * 7 * 3)
        return HttpResponseRedirect(ret)