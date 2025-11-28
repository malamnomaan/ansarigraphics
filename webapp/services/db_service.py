from django.db.models import Q
from webapp.models import Service, Category

def get_service(service_id=None):
    """
        get service
    """
    q = Q()
    if service_id:
        q&=Q(id=service_id)
    service_obj = Service.objects.filter(q)
    return service_obj

def add_new_service(data):
    """
        add new service
    """
    msg = "Service added successfully"
    if not data.get("id"):
        data.pop("id")
        Service.objects.create(**data)
    else:
        
        Service.objects.filter(id=data.get("id")).update(**data)
        msg = "Service updated successfully"
    return True, msg

def activation_service(service_id, status):
    """
        activate / deactive service
    """
    msg = "Service activated successfully"
    Service.objects.filter(id=service_id).update(is_active=status)
    if status == False:
        msg = "Service deactivated successfully"
    return True, msg

def get_category(category_id=None):
    """
        get category
    """
    q = Q()
    if category_id:
        q&=Q(id=category_id)
    category_obj = Category.objects.filter(q)
    return category_obj

def add_new_category(data):
    """
        add new category
    """
    msg = "Category added successfully"
    if not data.get("id"):
        data.pop("id")
        Category.objects.create(**data)
    else:
        Category.objects.filter(id=data.get("id")).update(**data)
        msg = "Category updated successfully"
    return True, msg