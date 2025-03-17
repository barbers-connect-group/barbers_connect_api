from rest_framework import serializers

from api.models import Review
from api.models import BarberShop

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    barbershop = serializers.PrimaryKeyRelatedField(queryset=BarberShop.objects.all())

    class Meta:
        model = Review
        fields = '__all__'
