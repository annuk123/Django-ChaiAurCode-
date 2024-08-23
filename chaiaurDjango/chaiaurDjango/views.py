from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    # return HttpResponse("Hello, world. You're at the Home page.")



    # return render(request, 'index.html')
    return render(request, 'home/index.html')

def about(request):
    # return HttpResponse("Hello, world. You're at the about page.")
    return render(request, 'about/index.html')

def contact(request):
    # return HttpResponse("Hello, world. You're at the contact page.")
    return render(request, 'contact/index.html')

