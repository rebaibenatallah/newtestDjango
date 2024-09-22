from django.shortcuts import render
from .models import User_portfolio
from .forms import user_portfolioform,skills

# Create your views here.
def portfolio(request):
    return render(request,'portfolio/index.html')

def page(request):
    user = User_portfolio.objects.all()
    x = {'user':user}
    return render(request,'portfolio/page.html',x)

def skill(request):
    data = skills(request.POST)
    if data.is_valid():
        data.save()
    return render(request,'portfolio/insert.html',{'userform':skills})

def insert(request):
    # ================= get data posted from insert html with forms.py
    dataform = user_portfolioform(request.POST,request.FILES)
    # print(dataform)
    if dataform.is_valid():
        dataform.save()
    # ================================================================
    # ================= get data posted from insert html ======
    # name = request.POST.get('name')
    # job = request.POST.get('job')
    # img = request.POST.get('img')
    # years_work = request.POST.get('years_work')
    # completed_projects = request.POST.get('completed_projects')
    # satisfied_costomers = request.POST.get('satisfied_costomers')
    # ================= send data to db user portfolio table ===
    # data =User_portfolio(Name=name,Job=job,image=img,Years_work=years_work,Completed_projects=completed_projects,Satisfied_costomers=satisfied_costomers)
    # data.save()
    # ==========================================================

    # print(name)
    # print(job)
    # print(img)
    # print(years_work)
    # print(completed_projects)
    # print(satisfied_costomers)
    return render(request,'portfolio/insert.html',{'userform':user_portfolioform})