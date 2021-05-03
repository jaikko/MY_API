from django.http import request
from .models import Comments, Contributors, Issues, Projects, User
from rest_framework import permissions, views

class IsProjectAuthor(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return True
        
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
       
        return obj.author == request.user   
            
        
class IsContributor(permissions.BasePermission):
    
    def has_permission(self, request, view):
        id = view.kwargs.get('project_pk')
        if Contributors.objects.filter(user= request.user, project_id = id).exists():
            if request.method == 'POST':
               return False
            return True
        elif Projects.objects.filter(author_id=request.user.id , id=id).exists():
            return True
        return False


    def has_object_permission(self, request, view, obj):
      
        return obj.project.author == request.user
        
            
        
class IssuesPerm(permissions.BasePermission):
        def has_permission(self, request, view):
            id = view.kwargs.get('project_pk')
            if Contributors.objects.filter(user= request.user, project_id = id).exists():
                return True
            return False
        
        def has_object_permission(self, request, view, obj):
            
            return obj.author == request.user    


class ComsPerm(permissions.BasePermission):
    
        def has_permission(self, request, view):
           
            id = view.kwargs.get('project_pk')
            if Contributors.objects.filter(user= request.user, project_id = id).exists():
                return True  
            if Projects.objects.filter(author=request.user , id=id).exists():
                if request.method == 'POST':
                    return False
                return True   
            return False
                                  
        def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return Contributors.objects.filter(user= request.user, project=obj.issue.project).exists()|Projects.objects.filter(author=request.user , id=obj.issue.project.id).exists()
            return obj.author == request.user           
            
            
                  
        

