from django.shortcuts import render
from .models import bilder

# Create your views here.
def index(request):
    bil= bilder.objects.all()
    return render(request,"index.html" , {'bil':bil})

def about(request):
    return render(request,"about-us.html")

def service(request):
    return render(request,"service.html")

def contact(request):
    return render(request,"contact.html")

def project(request):
    bil = bilder.objects.all()
    return render(request,"projects.html", {'bil':bil})

def element(request):
    return render(request,"elements.html")

def index1(request):
    bil = bilder.objects.all()
    return render(request, "index.html", {'bil': bil})

