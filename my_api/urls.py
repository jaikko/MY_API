from django.urls.conf import include
from .views import CommentsViewSet, IssuesViewSet, RegisterAPI, ProjectViewSet, ContributorViewSet
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework import routers
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename="Project")

project_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
project_router.register(r'users', ContributorViewSet, basename='project-users')
issues_routeur = routers.NestedSimpleRouter(router, r'projects', lookup='project')
issues_routeur.register(r'issues', IssuesViewSet, basename='project-issues')
comments_routeur = routers.NestedSimpleRouter(issues_routeur, r'issues', lookup='issue')
comments_routeur.register(r'comments', CommentsViewSet, basename='comment')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(issues_routeur.urls)),
    path('', include(comments_routeur.urls)),
    path('signup', RegisterAPI.as_view(), name='register'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
