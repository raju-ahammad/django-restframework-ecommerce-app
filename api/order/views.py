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

@csrf_exempt
def add(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse ({'error': 'please re-login', "code": '1'})
    
    if request.method == 'POST':
        user_id = id
        transaction_id = request.POST["transaction_id"]
        amount = request.POST['amount']
        products = request.POST['products']
        
        total_pro = len(products.split(',')[:-1])
        
        userModel = get_user_model()
        
        try:
            user = userModel.objects.get(pk=user_id)
        except userModel.DoesNotExist:
            return JsonResponse({'error': 'user does not exist'})
        
        order = Order(user=user, product_names=products, total_products=total_pro, transaction_id=transaction_id, total_amount=amount)
        order.save()
        return JsonResponse({"success": True, "error": True, 'msg':"order place succesfully"})        


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class  = OrderSerializer
