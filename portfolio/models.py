from django.db import models

# Create your models here.
class User_portfolio(models.Model):
    
    Name = models.CharField(max_length=250)
    Job = models.CharField(max_length=250)
    Years_work = models.IntegerField(max_length=5)
    Completed_projects = models.IntegerField(max_length=5)
    Satisfied_costomers = models.IntegerField(max_length=5)

