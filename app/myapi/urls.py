from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'roles', views.EmployeeRoleViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'contracts', views.ContractViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'members', views.TeamMemberViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
