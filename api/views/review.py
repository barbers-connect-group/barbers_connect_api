from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from api.models import Review
from api.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


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
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = BarberShopPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Review.objects.all()
        barbershop_id = self.request.query_params.get('barbershop_id')
        if barbershop_id is not None:
            queryset = queryset.filter(barbershop_id=barbershop_id)

        return queryset
