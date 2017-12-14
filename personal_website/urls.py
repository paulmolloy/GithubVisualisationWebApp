from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^github$', views.github, name='github'),
        url(r'^visualisation$', views.visualisation, name='visualisation'),
        url(r'^api/commit_count_google_ubp', views.commit_count_google_ubp, name='commit_count_google_ubp'),        
        url(r'^graph$', views.graph, name = 'graph')
    ]
