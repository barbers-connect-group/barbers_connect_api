from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from api.views import login, signup, test_token

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

    # API
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/download/', SpectacularAPIView.as_view(), name='schema'),
    re_path('signup', signup),
    re_path('login', login),
    re_path('test_token', test_token),
]
