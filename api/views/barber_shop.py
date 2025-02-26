from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.response import Response

from api.models import BarberShop


class BarberShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarberShop
        fields = '__all__'


class BarberShopPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


@extend_schema(
    parameters=[
        OpenApiParameter(
            'Authorization',
            description="Token necessário no formato 'token <seu_token>'",
            required=True,
            type=str
        )
    ]
)
class BarberShopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BarberShop.objects.all()
    serializer_class = BarberShopSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = BarberShopPagination

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
