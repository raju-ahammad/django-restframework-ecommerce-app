from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)


urlpatterns = [
    path('login/', views.signIn, name='signin'),
    path('logout/<int:id>/', views.signOut, name='signout'),
    path('', include(router.urls))
]

