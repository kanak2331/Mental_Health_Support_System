from django.shortcuts import render

# Create your views here.
def jounnaling(request):
    return render(request,'auth/jounnaling.html')