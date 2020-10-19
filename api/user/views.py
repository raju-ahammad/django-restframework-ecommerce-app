# Create your views here.
import random
import re

from django.contrib.auth import get_user_model, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import CustomUser
from .serializers import UserSerializers


def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)]+ [str(i) for i in range(10)]) for _ in range(length))

@csrf_exempt
def signIn(request):
    if not request.method == "POST":
        return JsonResponse({'error': 'Send a post request with valid paramenter'})
    
    username = request.POST['email']
    password = request.POST['password']
    
    #validation part
    # if not re.match("^([\w\.\-_]+)?\w+@[\w-_]+(\.\w+){1,}$", username):
    #     return JsonResponse({'error': 'Enter a valid email address.'})
    if len(password) < 3:
        return JsonResponse({'error': 'password need to be at least 3 letter'})
    
    UserModel = get_user_model()
    
    try:
        user = UserModel.objects.get(email=username)
        
        if user.check_password(password):
            user_dict  = UserModel.objects.filter(email=username).values().first()
            user_dict.pop('password')
            
            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error': 'previous session exist'})
         
            token = generate_session_token()
            user.session_token = token
            user.save() 
            login(request, user)
            return JsonResponse({'token': token, 'user': user_dict})    
        else:
            return JsonResponse({'error':'inavalid password'})
    
        
        
    except UserModel.DoesNotExist:
        return JsonResponse({'error': "Invalid email"})
    
    
def signOut(request, id):
    logout(request)
    
    userModel = get_user_model()
    
    try:
        user = userModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except userModel.DoesNotExist:
        return JsonResponse({'error': 'Inavalid User Id'})
    return JsonResponse({'success':'Logout success' })

class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}
    
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializers
    
    def get_permissions(self):
        
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
        