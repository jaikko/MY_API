
from django.conf.urls import url
from django.urls.conf import include
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework_extensions.routers import ExtendedSimpleRouter
from .views import RegisterAPI,ProjectViewSet, ContributorViewSet, UserViewSet
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename="Project")

router = ExtendedSimpleRouter()
(
    router.register(r'projects', ProjectViewSet, basename='project')
          .register(r'users',
                    ContributorViewSet,
                    basename='projects-users',
                    parents_query_lookups=['projects'])
          
)

urlpatterns = [
    path('', include(router.urls)),
    path('signup', RegisterAPI.as_view(), name='register'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
]