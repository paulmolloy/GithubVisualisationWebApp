from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from github import Github

def index(request):
        return HttpResponse("Hello, World!")

GITHUB_TOKEN = "70c438ead2254788400a09559d93855961e3a80e"
def github(request):
        #g = Github("paulmolloy", GITHUB_TOKEN)
        #repos = [];
        #for repo in g.get_user().get_repos():
        #    repos.append(repo.name)
        repos = list_org_repos('Google')    
        template = loader.get_template('personal_website/index.html')
        context = {
                'repos': repos
                }
        return HttpResponse(template.render(context, request))
    
        #return HttpResponse("Github stuff" + ' '.join(repos))
def visualisation(request):
        vals = [1,3,5,70];
            
        template = loader.get_template('personal_website/visualisation.html')
        context = {
                'vals': vals
                }
        return HttpResponse(template.render(context, request))
    


def list_org_repos(name):
    repos = [];
    g = Github('paulmolloy', GITHUB_TOKEN)
    print ("got token")
    org = g.get_organization(name)
    print ("got org")
    for repo in org.get_repos():
        print ('appending' + repo.name)
        repos.append(repo.name)

    return repos
