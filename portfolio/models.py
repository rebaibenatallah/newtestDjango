from django.db import models

# Create your models here.
class User_portfolio(models.Model):
    Name = models.CharField(max_length=250)
    Job = models.CharField(max_length=250)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    Years_work = models.IntegerField()
    Completed_projects = models.IntegerField()
    Satisfied_costomers = models.IntegerField()

# content = models.TextField()
# price = models.DecimalField(max_digits=5 , decimal_places=2) 
# image = models.ImageField(upload_to='photos/%y/%m/%d')

class Skills(models.Model):
    Name = models.CharField(max_length=255)