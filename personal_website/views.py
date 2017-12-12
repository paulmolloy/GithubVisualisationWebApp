from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from github import Github

def index(request):
        return HttpResponse("Hello, World!")

GITHUB_TOKEN = "key"
def github(request):
        g = Github("paulmolloy", GITHUB_TOKEN)
        repos = [];
        for repo in g.get_user().get_repos():
            repos.append(repo.name)
            
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
    
    
