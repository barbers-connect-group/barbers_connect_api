from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.response import Response
from django.db.models import Subquery

from api.models import BarberShop
from api.models import Tag
from api.serializers import BarberShopSerializer


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
    serializer_class = BarberShopSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = BarberShopPagination

    def get_queryset(self):
        queryset = BarberShop.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        tag_name = self.request.query_params.get('tag_name')
        if tag_name is not None:
            queryset = queryset.filter(
                tags__id__in=Subquery(
                    Tag.objects.filter(name__icontains=tag_name)
                    .values_list('id', flat=True)
                )
            )

        return queryset


    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
