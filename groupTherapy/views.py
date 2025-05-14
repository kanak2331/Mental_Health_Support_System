from django.shortcuts import render

# Create your views here.
def groupTherapy(request):
    return render(request,'auth/groupTherapy.html')