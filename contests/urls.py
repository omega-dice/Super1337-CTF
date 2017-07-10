from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<name>[a-z0-9.-]+)/$', views.contest_view, name='contest_view'),
    url(r'^(?P<name>[a-z0-9.-]+)/register/$', views.contest_register, name='contest_register')
]