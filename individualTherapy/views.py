from django.shortcuts import render

# Create your views here.
def individualTherapy(request):
    return render(request,'auth/individualTherapy.html')