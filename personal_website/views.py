from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
        return HttpResponse("Hello, World!")

GITHUB_TOKEN = "TOKENHERE"
def github(request):
        from github import Github
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
    
