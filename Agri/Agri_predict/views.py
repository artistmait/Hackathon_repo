from django.shortcuts import render, HttpResponse



def home(request):
    return render(request,'prediction.html')

# Create your views here.
