from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'', views.OrderViewSet)


urlpatterns = [
    path('add/<str:id>/<str:token>/', views.add, name='order_add'),
    path('', include(router.urls))
]

