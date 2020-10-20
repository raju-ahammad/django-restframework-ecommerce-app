import braintree
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="n6sdwwtn9v8cgybk",
        public_key="yktwz5c52hjtxgsj",
        private_key="a5a1738e3aa557e11fa54c3b7b675bd1"
    )
)

def validate_user_session(id, token):
    UserModel = get_user_model()
    
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_tokenn = token:
            return True
        return False
        
    except UserModel.DoesNotExist:
        return False

@csrf_exempt 
def generate_token(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': "Invalid session, please login agin"})
    
    return JsonResponse({'clientToken': gateway.client_token.generate(), 'success':True})
