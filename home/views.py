from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def ecommerce(request):
    return render(request,'ecommerce.html')
