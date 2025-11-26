from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, 'public/index.html')

def about(request):
    return render(request, 'public/about.html')

def contact(request):
    return render(request, 'public/contact.html')

def gallery(request):
    return render(request, 'public/gallery.html')

def services(request):
    return render(request, 'public/services.html')

def login(request):
    return render(request, 'public/login.html')