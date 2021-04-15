from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authapp.views_api import UserListAPIView
# from mainapp.views_api import ProjectViewSet, TodoListViewSet
from mainapp.views_api import ProjectViewSet, TodoListViewSet

router = DefaultRouter()
# router.register('users', UserListAPIView)
router.register('projects', ProjectViewSet)
router.register('todos', TodoListViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Project",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('admin-staff/', include('adminapp.urls', namespace='admin_staff')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # re_path(r'^api/(?P<version>\d\.\d)/users/$', UserListAPIView.as_view()),
    path('api/users/0.1', include('authapp.urls', namespace='0.1')),
    path('api/users/0.2', include('authapp.urls', namespace='0.2')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
