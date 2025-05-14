from django.urls import path 
from . import views

urlpatterns=[
    path('',views.groupTherapy,name="groupTherapy"),
]