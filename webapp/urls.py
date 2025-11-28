from django.urls import path
from webapp.views import *

urlpatterns = [
    path('', landing, name="landing"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('gallery', gallery, name="gallery"),
    path('services', services, name="services"),
    path('login', login_page, name="login"),
    path('login_user/', login_user, name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),
    path('add_update_service', add_update_service, name='add_update_service'),
    path('get_service_by_id', get_service_by_id, name='get_service_by_id'),
    path('add_update_category', add_update_category, name='add_update_category'),
    path('category_info', category_info, name='category_info'),
    path('add_gallery_item', add_gallery_item, name='add_gallery_item'),
]