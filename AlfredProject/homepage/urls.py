from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.auth, name='auth'),
    url(r'^echo$', views.echo, name='echo'),
    url(r'^echo/logout$', views.logout, name='logout'),
    url(r'^echo/dev/detail/(?P<name>[a-zA-Z0-9_]+)/$', views.detail, name='dev'),
    url(r'^echo/dev$', views.dev, name='dev'),
    url(r'^echo/addvenue/(?P<venue>[a-zA-Z0-9_]+):(?P<phone>[a-zA-Z0-9_]+)/$', views.addvenue, name='addvenue'),
    url(r'^echo/getvenue/$', views.getvenue, name='getvenue'),
    url(r'^echo/delvenue/(?P<venue>[a-zA-Z0-9_]+)/$', views.delvenue, name='delvenue'),
    url(r'^echo/adduser/(?P<name>[a-zA-Z0-9_]+):(?P<email>[a-zA-Z0-9_@.]+)/$', views.adduser, name='adduser'),
    url(r'^echo/getuser/$', views.getuser, name='getuser'),
    url(r'^echo/deluser/(?P<name>[a-zA-Z0-9_]+)/$', views.deluser, name='deluser'),
    url(r'^echo/queryresp/(?P<venue>[a-zA-Z0-9_]+):(?P<order>[a-zA-Z0-9_]+):(?P<cost>[a-zA-Z0-9.]+)/$', views.queryresp, name='queryresp')
]
