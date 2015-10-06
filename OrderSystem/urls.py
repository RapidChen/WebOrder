from django.conf.urls import patterns, url
from OrderSystem import views


urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),
)