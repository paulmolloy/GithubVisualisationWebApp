from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Organization(models.Model):
    organization_name = models.CharField(max_length=200)

class Repository(models.Model):
    repo_name = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization)
    open_issues_count = models.IntegerField()
    size = models.IntegerField() 
    num_stars = models.IntegerField()

class Commit(models.Model):
    url = models.CharField(max_length=300)
    author_name =  models.CharField(max_length=200) 
    message = models.CharField(max_length=500)
    num_files = models.IntegerField()
    additions = models.IntegerField()
    deletions = models.IntegerField()
    total_change = models.IntegerField()
    repo = models.ForeignKey(Repository)
    organization = models.ForeignKey(Organization)




