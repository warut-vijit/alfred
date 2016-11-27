from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.warn, name='warn'),
    url(r'^echo$', views.index, name='index'),
    url(r'^echo/(?P<text>[a-z]+)$', views.echo, name='echo'),
    url(r'^echo/(?P<text>[a-z]+)/$', views.echo, name='echo'),
]
