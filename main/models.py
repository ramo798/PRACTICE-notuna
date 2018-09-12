from django.db import models

class Userinfor(models.Model):
    userid = models.CharField(max_length=20)
    profname = models.CharField(max_length=20)
    profpic = models.TextField()
    proftext = models.CharField(max_length=100)

class Post(models.Model):
    userids = models.CharField(max_length=20)
    posttext = models.CharField(max_length=100)


    
