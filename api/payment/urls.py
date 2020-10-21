from django.urls import include, path

from . import views

urlpatterns = [
    path('gettoken/<str:id>/<str:token>/', views.generate_token, name="token.genarate"),
    path('process/<str:id>/<str:token>/', views.process_payment, name="payment.process")
    
]
