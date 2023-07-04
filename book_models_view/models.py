from django.db import models


# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    info = models.TextField()
    Date_of_issue = models.DateField()
