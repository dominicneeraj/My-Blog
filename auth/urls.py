from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt
from auth import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^hello$', 'index.views.hello', name = 'hello'),

    url(r'^login$',csrf_exempt(views.login),name='login'),
    url(r'^logout$','auth.views.logout_auth', name='logout'),

)
urlpatterns += staticfiles_urlpatterns()
