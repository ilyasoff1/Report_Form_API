
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


schema_view = get_schema_view(
    openapi.Info(
        title='Task API',
        description='Django Rest Framework Task Scheduler API',
        default_version='v1',
        terms_of_service='https://google.com/policies/terms/',
        contact=openapi.Contact(email='ilyosov.fa@gmail.com'),
        license=openapi.License(name='Task project licence'),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )


urlpatterns = [
    path('report/', include('report.urls')),
    path('profile/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
