from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from webapp.services.db_service import get_service, add_new_service

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
    all_services = get_service()
    print(all_services)
    return render(request, 'public/services.html', {"all_services": all_services})

def login_page(request):
    return render(request, 'public/login.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("services")   # Redirect after login
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")       # Redirect back to login page

    # If someone tries /login_user directly → send them to login page
    return redirect("login")

def logout_user(request):
    logout(request)
    return redirect("login")

@csrf_exempt  # disables CSRF check
@api_view(['POST'])
def add_update_service(request):
    data = request.data
    success, message = add_new_service(data)
    return Response({"status": success, "message": message}, status=status.HTTP_200_OK)