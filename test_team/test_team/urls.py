from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Team API",
        default_version='v1',
        description="API about team management",
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('main.urls')),
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
