from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from github import Github
from personal_website.models import Organization, Repository, Commit

def index(request):
        return HttpResponse("Hello, World!")

GITHUB_TOKEN = "70c438ead2254788400a09559d93855961e3a80e"
def github(request):
        template = loader.get_template('personal_website/index.html')
        org = 'Google'
        query_github(org)
        org_id = Organization.objects.filter(organization_name = org)[0]
        repos = Repository.objects.filter(organization = org_id).values_list('repo_name', flat=True).order_by('id')
        context = {
                'repos': repos
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
    if(len(Organization.objects.filter(organization_name=name))>0):
        return

    Organization(organization_name=name).save()
    repos = []
    org_id = Organization.objects.filter(organization_name=name)[0]
    for repo in org.get_repos():
        repos.append(repo.name)
        if(len(Repository.objects.filter(repo_name=repo.name, organization = org_id))==0):
            Repository(repo_name= repo.name, organization = org_id).save()
    
    if(len(repos)==0):
        return 
    repo = org.get_repo(repos[0])
          
    
    return  

def list_org_repos(g, name):
    repos = [];
    org = g.get_organization(name)
    print ("got org")
    for repo in org.get_repos():
        print ('appending' + repo.name)
        repos.append(repo.name)

    return
