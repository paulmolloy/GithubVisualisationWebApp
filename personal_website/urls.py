from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^github$', views.github, name='github'),
        url(r'^visualisation$', views.visualisation, name='visualisation'),
        
    ]
