
from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       # url(r'^hello$', 'index.views.hello', name = 'hello'),

                       url(r'^$', 'main.views.index', name='index'),
                       url(r'^contact$', 'main.views.contact', name='contact'),
                       url(r'^about$', 'main.views.about', name='about'),
                       url(r'^registration$', 'main.views.registration', name='registration'),
                       url(r'^services$', 'main.views.services', name='services'),
                       )
