from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from github import Github
from github import GithubException
from personal_website.models import Organization, Repository, Commit
from datetime import timedelta, date, time, datetime as dt
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
        return HttpResponse("Hello, World!")

GITHUB_TOKEN = "70c438ead2254788400a09559d93855961e3a80e"
def github(request):
        template = loader.get_template('personal_website/index.html')
        org = 'Google'
        query_github(org)
        org_id = Organization.objects.filter(organization_name = org)[0]
        repos = Repository.objects.filter(organization = org_id).values_list('repo_name', flat=True).order_by('id')
        repo_id = Repository.objects.filter(organization = org_id, repo_name=repos[0]) 
        commits = Commit.objects.filter(organization= org_id, repo = repo_id).values
        context = {
                'repos': repos,
                'commits' : commits
                }
        
        return HttpResponse(template.render(context, request))
    
def visualisation(request):
        vals = [1,3,5,70];
            
        template = loader.get_template('personal_website/visualisation.html')
        context = {
                'vals': vals
                }
        return HttpResponse(template.render(context, request))
  

def query_github(name):
    g = Github('paulmolloy', GITHUB_TOKEN)
    org = g.get_organization(name)
    if(len(Organization.objects.filter(organization_name=name))==0):
        Organization(organization_name=name).save()

    repos = []
    org_id = Organization.objects.filter(organization_name=name)[0]
    for repo in org.get_repos():
        if(len(Repository.objects.filter(repo_name=repo.name, organization = org_id))==0):
            print 'getting repo' + repo.name
            repos.append(repo.name)
            Repository(repo_name= repo.name, organization = org_id, open_issues_count = repo.open_issues_count, size = repo.size,
                    num_stars = repo.stargazers_count).save()
            repo_id = Repository.objects.filter(repo_name = repo.name, organization = org_id)[0]
            num_days = 365
            query_commits(repo, org_id, repo_id, num_days);
        else:
            print 'skipping ' + repo.name
    return  

def query_commits(repo, org_id, repo_id, num_days):
    td = timedelta(days = num_days)
    since_time = dt.now() - td
    try:
        commits = repo.get_commits(since = since_time)
        for commit in commits:
            print commit.commit.committer.name
            #if(len(Commit.objects.filter(repo=repo_id, organization = org_id, url=commit.commit.url))==0):
            print 'adding'
            Commit(url = commit.commit.url, author_name = commit.commit.committer.name, message = commit.commit.message, 
            num_files = len(commit.files), additions = commit.stats.additions, deletions = commit.stats.deletions, 
            total_change = commit.stats.total, repo=repo_id, organization = org_id).save() 
    except GithubException as e:
        print(e.args[1]['message'])
    


def list_org_repos(g, name):
    repos = [];
    org = g.get_organization(name)
    print ("got org")
    for repo in org.get_repos():
        print ('appending' + repo.name)
        repos.append(repo.name)

    return

def graph(request):
        return render(request, 'personal_website/graph.html')

def repositories_graph(request):
        return render(request, 'personal_website/repos_graph.html')

def commit_count_google(request, repo_name=None):
    name = 'Google'
    repo_name = 'paco'
    org_id = Organization.objects.filter(organization_name=name)[0]
    repo_id = Repository.objects.filter(organization = org_id, repo_name = repo_name)[0]
    data = Commit.objects.filter(repo= repo_id).values('author_name').annotate(count_items=Count('id'))

    print 'repo_id' + repo_name
    print  list(data)
    return JsonResponse(list(data), safe=False)

 
def commit_count_google_ubp(request):
    name = 'Google'
    #repo_name = 'upb'
    org_id = Organization.objects.filter(organization_name=name)[0]
    repo_id = Repository.objects.filter(organization = org_id)[0]
    data = Commit.objects.filter(repo= repo_id).values('author_name').annotate(count_items=Count('id'))

    return JsonResponse(list(data), safe=False)


def repos_issues_stars_size(request):
    name = 'Google'
    org_id = Organization.objects.filter(organization_name=name)[0]
    #for repo in org.get_repos():
    repo_data = Repository.objects.filter(organization=org_id).values('repo_name', 'open_issues_count', 'size', 'num_stars')

    return JsonResponse(list(repo_data), safe=False)
