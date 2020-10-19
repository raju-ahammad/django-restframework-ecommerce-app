from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from .models import Order
from .serializers import OrderSerializer

# Create your views here.

def validate_user_session(id, token):
    userModel = get_user_model()
    
    try:
        user = userModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except userModel.DoesNotExist:
        return False
