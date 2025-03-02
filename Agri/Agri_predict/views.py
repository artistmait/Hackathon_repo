from django.shortcuts import render, HttpResponse



def home(request):
    return render(request,'prediction.html')


def landingpage(request):
    return render(request,'landingpage.html')

# Create your views here.
