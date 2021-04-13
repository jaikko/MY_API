
from .models import Projects, User, Contributors
from rest_framework import permissions, serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name','email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save() 

        return user
    
# Register Serializer
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id','title','description','type', 'author')
        
    def create(self,validated_data):
        projet = Projects.objects.create(title=validated_data['title'],
            description=validated_data['description'],type=validated_data['type'],
            author_id=self.context['request'].user.id
        )
        
        projet.save() 
     
        return projet

class ContributorSerializer(serializers.ModelSerializer):
    projectby = UserSerializer(many= True, read_only = True)
    class Meta:
        model = Contributors
        fields = ('role','premission','project', 'user')
        
    def create(self,validated_data):

        contri = Contributors.objects.create(role=validated_data['role'],
            permission=validated_data['permission'],project_id=validated_data['project_id'],
            user_id=self.context['request'].user.id
        )
        
        contri.save() 
     
        return contri

    