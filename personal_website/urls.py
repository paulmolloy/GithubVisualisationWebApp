from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^github$', views.github, name='github'),
        url(r'^visualisation$', views.visualisation, name='visualisation'),
        url(r'^api/commit_count_google_ubp', views.commit_count_google_ubp, name='commit_count_google_ubp'),        
        url(r'^api/repos_issues_stars_size', views.repos_issues_stars_size, name='repos_issues_stars_size'),        
        url(r'^graph$', views.graph, name = 'graph'),
        url(r'^repositories_graph$', views.repositories_graph, name = 'repositories_graph')
        
    ]
