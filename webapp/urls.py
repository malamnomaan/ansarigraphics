from django.urls import path
from webapp.views import landing, about, contact, gallery, services, login_page, login_user, logout_user, add_update_service, get_service_by_id

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
]