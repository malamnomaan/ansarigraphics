import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from webapp.services.db_service import get_service, add_new_service, get_category
from webapp.models import Category, GalleryItem

# Create your views here.
def landing(request):
    return render(request, 'public/index.html')

def about(request):
    return render(request, 'public/about.html')

def contact(request):
    return render(request, 'public/contact.html')

def gallery(request):
    all_categories = get_category()
    return render(request, 'public/gallery.html', {"all_categories": all_categories})

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

@csrf_exempt  # disables CSRF check
@api_view(['POST'])
def get_service_by_id(request):
    data = request.data
    data = get_service(data.get("service_id"))

    resp_data = {
        "id": data[0].id,
        "title": data[0].title,
        "full_description": data[0].full_description,
        "icon": data[0].icon,
        "is_active": data[0].is_active,
    }
    return Response({"status": True, "message": "service data fetch successfully", "data": resp_data}, status=status.HTTP_200_OK)

@csrf_exempt  # disables CSRF check
@api_view(['POST'])
def add_update_category(request):
    """
    Single POST API for Add + Update Category
    Accepts: multipart/form-data
    """

    if request.method != "POST":
        return Response({"status": False, "message": "Invalid method"}, status=400)

    category_id = request.POST.get("id")
    name = request.POST.get("name")
    description = request.POST.get("description")
    uploaded_file = request.FILES.get("img_path")   # <-- FIXED NAME

    # Validate
    if not name:
        return Response({"status": False, "message": "Name is required"}, status=400)

    # --------------- SAVE IMAGE IF EXISTS ----------------
    saved_img_path = None   # <-- FINAL path saved to DB

    if uploaded_file:  # only if file exists
        folder = os.path.join(settings.BASE_DIR, "static/categories")
        os.makedirs(folder, exist_ok=True)

        file_path = os.path.join(folder, uploaded_file.name)

        # save image to static folder
        with open(file_path, "wb+") as dest:
            for chunk in uploaded_file.chunks():
                dest.write(chunk)

        saved_img_path =  "static/categories/" + uploaded_file.name  # <-- path saved to DB

    # ---------------- ADD NEW CATEGORY -------------------
    if not category_id:
        Category.objects.create(
            name=name,
            description=description,
            img_path=saved_img_path
        )
        return Response({"status": True, "message": "Category added successfully"})

    # ---------------- UPDATE EXISTING CATEGORY -----------
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({"status": False, "message": "Category not found"}, status=404)

    category.name = name
    category.description = description

    # update only if new file uploaded
    if saved_img_path:
        category.img_path = saved_img_path

    category.save()

    return Response({"status": True, "message": "Category updated successfully"})

def category_info(request):
    try:
        category_id = request.GET.get("category_id")
        category = Category.objects.get(id=category_id)
        gallery_items = GalleryItem.objects.filter(category=category, is_active=True)
    except Category.DoesNotExist:
        return redirect("gallery")  # Redirect if category not found

    return render(request, 'public/category-details.html', {"category": category, 'gallery_items': gallery_items})

def add_gallery_item(request):
    if request.method == "POST" and request.FILES.get("category_image"):
        uploaded_file = request.FILES["category_image"]
        category_id = request.POST.get("category_id")
        description = request.POST.get("description", "")
        title = request.POST.get("title", "")
        folder = os.path.join(settings.BASE_DIR, "static/categories")
        os.makedirs(folder, exist_ok=True)

        file_path = os.path.join(folder, uploaded_file.name)

        # save image to static folder
        with open(file_path, "wb+") as dest:
            for chunk in uploaded_file.chunks():
                dest.write(chunk)
        
        # save image path to DB
        gallery_item = GalleryItem.objects.create(
            title=title,
            image_url="static/categories/" + uploaded_file.name,
            description=description,
            category_id=category_id
        )

        return Response({"status": True, "message": "Image uploaded successfully", "img_path": "static/categories/" + uploaded_file.name})

    return Response({"status": False, "message": "No image uploaded"}, status=400)