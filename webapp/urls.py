from django.urls import path
from webapp.views import landing, about, contact, gallery, services

urlpatterns = [
    path('', landing),
    path('about', about),
    path('contact', contact),
    path('gallery', gallery),
    path('services', services),
    
]