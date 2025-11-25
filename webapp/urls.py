from django.urls import path
from webapp.views import landing

urlpatterns = [
    path('', landing)
]