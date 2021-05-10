
import json
from django.http import request
from django.http.response import Http404
from django.shortcuts import render
from .models import Comments, Contributors, Issues, Projects, User
from rest_framework import authentication, generics, permissions
from rest_framework.response import Response
from .serializers import CommentsSerializer, ContributorSerializer, IssuesSerializer, UserSerializer, RegisterSerializer, ProjectSerializer
from rest_framework import viewsets
from .permissions import IsContributor, IsProjectAuthor, ComsPerm, IssuesPerm

# Create your views here.


# Register User in API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user": UserSerializer(user, context=self.get_serializer_context()).data})


# User
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all


# Project
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated, IsProjectAuthor)

    def get_queryset(self):
        return Projects.objects.filter(contributors__user=self.request.user) | Projects.objects.filter(author=self.request.user)


# Contributor
class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = (permissions.IsAuthenticated, IsContributor)

    def get_queryset(self):
        id = self.kwargs['project_pk']
        return Projects.objects.get(pk=id).contributors


# Issues
class IssuesViewSet(viewsets.ModelViewSet):
    serializer_class = IssuesSerializer
    permission_classes = (permissions.IsAuthenticated, IssuesPerm)

    def get_queryset(self):
        id = self.kwargs['project_pk']
        return Issues.objects.filter(project_id=id)


# Comments
class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = (permissions.IsAuthenticated, ComsPerm)

    def get_queryset(self):
        id = self.kwargs['issue_pk']
        return Issues.objects.get(pk=id).comments
