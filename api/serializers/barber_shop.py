from rest_framework import serializers
from api.models import BarberShop


class BarberShopSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = BarberShop
        fields = '__all__'

    def get_tags(self, obj):
        return [{"id": tag.id, "name": tag.name} for tag in obj.tags.all()]
