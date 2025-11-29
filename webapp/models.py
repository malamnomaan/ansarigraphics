from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=150)
    full_description = models.TextField(blank=True)
    icon = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    img_path = models.CharField(max_length=200, blank=True)

class GalleryItem(models.Model):
    title = models.CharField(max_length=150)
    image_url = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='gallery_items')