from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.auth_main, name="auth_main"),
    url(r'^verify/username=(?P<username>[a-zA-Z0-9]+):password=(?P<password>[a-zA-Z0-9]+)$', views.auth_verify, name="auth_verify"),
    url(r'^err/(?P<username>[a-zA-Z0-9]+)$', views.auth_err, name="auth_err"),
    url(r'^err/(?P<username>[a-zA-Z0-9]+)/$', views.auth_err, name="auth_err")
]