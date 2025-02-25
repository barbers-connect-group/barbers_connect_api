from rest_framework import serializers
from api.models import BarberShop


class BarberShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarberShop
        fields = '__all__'
