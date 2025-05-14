from django.urls import path 
from . import views

urlpatterns=[
    path('',views.individualTherapy,name="individualTherapy"),
]