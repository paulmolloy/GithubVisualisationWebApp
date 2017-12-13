from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Organization(models.Model):
    organization_name = models.CharField(max_length=200)

class Repository(models.Model):
    repo_id = models.IntegerField()
    repo_name = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization)

class Commit(models.Model):
    commit_id = models.IntegerField();
    title = models.CharField(max_length=200)
    author =  models.CharField(max_length=200) 
    repository = models.ForeignKey(Repository)


