from django.db.models import Q
from webapp.models import Service

def get_service(service_id=ModuleNotFoundError):
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
    data = {
        "title": "Custom Web Development",
        "full_description": "Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem. Nulla quis lorem ut libero malesuada feugiat. Curabitur non nulla sit amet nisl tempus convallis. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "icon": "bi bi-code-slash",

    }
    Service.objects.create(**data)
    return True

def activation_service(service_id, status):
    """
        activate / deactive service
    """
    msg = "Service activated successfully"
    Service.objects.filter(id=service_id).update(is_active=status)
    if status == False:
        msg = "Service deactivated successfully"
    return True, msg