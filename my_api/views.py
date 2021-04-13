
import json
from django.shortcuts import render
from .models import Contributors, Projects, User
from rest_framework import authentication, generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer, ProjectSerializer
from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin


# Create your views here.

# Register User in API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        })
        

# Register User in API
class UserViewSet(viewsets.ModelViewSet, NestedViewSetMixin):
    serializer_class = UserSerializer
    def get_queryset(self):
        
        return User.objects.all   
    
 
        

# Project 
class ProjectViewSet(viewsets.ModelViewSet, NestedViewSetMixin):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        
        
        return Projects.objects.filter(author = self.request.user)
    
  
        
# Contibutor
class ContributorViewSet(viewsets.ModelViewSet, NestedViewSetMixin):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        
        return User.objects.all()





