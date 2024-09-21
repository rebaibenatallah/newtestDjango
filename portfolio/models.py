from django.db import models

# Create your models here.
class User_portfolio(models.Model):
    # ID = models.AutoField(unique=True)
    Name = models.CharField(max_length=250)
    Job = models.CharField(max_length=250)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    Years_work = models.IntegerField(null=True)
    Completed_projects = models.IntegerField(null=True)
    Satisfied_costomers = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.Name
# content = models.TextField()
# price = models.DecimalField(max_digits=5 , decimal_places=2) 
# image = models.ImageField(upload_to='photos/%y/%m/%d')

class Skills(models.Model):
    # ID = models.AutoField(unique=True)
    Name = models.CharField(max_length=255)

class Project(models.Model):
    Name = models.CharField(max_length=255)
    Category = models.CharField(max_length=255)
    Linkbigint = models.CharField(max_length=255)
    img = models.ImageField(upload_to='photos/%y/%m/%d')
    user_portfolio = models.ForeignKey(User_portfolio,on_delete=models.CASCADE)

class Skill(models.Model):
    Description = models.CharField(max_length=255)
    Level = models.CharField(max_length=255)
    user = models.ForeignKey(User_portfolio,on_delete=models.CASCADE)
    G_skills = models.ForeignKey(Skills,on_delete=models.CASCADE)