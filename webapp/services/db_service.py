from django.db.models import Q
from django.core.files.storage import default_storage
from webapp.models import Service, Category

def get_service(service_id=None, admin_view=False):
    """
        get service
    """
    q = Q()
    if service_id:
        q&=Q(id=service_id)
    if not admin_view:
        q&=Q(is_active=True)
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

def get_category(category_id=None, admin_view=False):
    """
        get category
    """
    q = Q()
    if category_id:
        q&=Q(id=category_id)
    if not admin_view:
        q&=Q(is_active=True)
    category_obj = Category.objects.filter(q)
    return category_obj
