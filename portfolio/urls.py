from django.urls import path
from . import views

urlpatterns =[
    path('s',views.portfolio,name='portfolio'),
    path('',views.page,name='page'),
    path('insert',views.insert,name='insert'),
]