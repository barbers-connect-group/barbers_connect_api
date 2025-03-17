from rest_framework import routers
from django.urls import path, include

from api.views import *

router = routers.DefaultRouter()
router.register(r'barbershops', BarberShopViewSet, basename='barbershop')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]