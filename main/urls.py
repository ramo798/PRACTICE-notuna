from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^form$', views.tweet, name='tweet'),
    url(r'^usename/$', views.namaeget, name='namaeget'),
]
