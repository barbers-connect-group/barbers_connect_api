from rest_framework import viewsets
from api.models import Review
from api.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
