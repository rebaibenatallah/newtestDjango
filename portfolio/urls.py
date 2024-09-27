from django.urls import path
from . import views

urlpatterns =[
    path('ss',views.portfolio,name='portfolio'),
    path('',views.page,name='page'),
    path('insert',views.insert,name='insert'),
    path('skills',views.skill,name='skills'),
    path('home',views.home,name='home'),
]