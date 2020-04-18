from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'roles', views.EmployeeRoleViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'members', views.TeamMemberViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]