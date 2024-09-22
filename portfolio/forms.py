from django import forms
from .models import User_portfolio , Skills

class skills(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'

class user_portfolioform(forms.ModelForm):
    # ==================== the first way =============
    # Name = forms.CharField(max_length=250)
    # Job = forms.CharField(max_length=250)
    # image = forms.ImageField()
    # Years_work = forms.IntegerField()
    # Completed_projects = forms.IntegerField()
    # Satisfied_costomers = forms.IntegerField()
    # ================================================
    class Meta:
        model =User_portfolio
        fields = ['Name','Job','image','Years_work','Completed_projects','Satisfied_costomers']
        # ====== if you need to use all th fields 
        # fields = '__all__'