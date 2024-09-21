from django.shortcuts import render
from .models import User_portfolio
# Create your views here.
def portfolio(request):
    return render(request,'portfolio/index.html')

def page(request):
    return render(request,'portfolio/page.html',{'user':User_portfolio.objects.all()})