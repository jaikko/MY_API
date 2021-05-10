from .models import Comments, Issues, Projects, User, Contributors
from rest_framework import permissions, response, serializers
from django.contrib.auth import get_user_model
from drf_nested_resources.fields import HyperlinkedNestedModelSerializer
from rest_framework.validators import UniqueTogetherValidator


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
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
        fields = ('id', 'title', 'description', 'type', 'author')

    def create(self, validated_data):

        projet = Projects.objects.create(title=validated_data['title'],
                                         description=validated_data['description'],
                                         type=validated_data['type'],
                                         author_id=self.context['request'].user.id)

        projet.save()
        return projet


class ContributorSerializer(serializers.ModelSerializer):

    # user = UserSerializer()

    class Meta:
        model = Contributors
        fields = ('id', 'role', 'permission', 'user', 'project')

    def validate(self, data):
        user = data.get('user')
        id = self.context.get('view').kwargs.get('project_pk')
        record = Contributors.objects.filter(user=user, project=id).first()

        if record:
            raise serializers.ValidationError({"detail": "This user is already added"})

        return super().validate(data)

    def create(self, validated_data):
        id = self.context.get('view').kwargs.get('project_pk')
        contri = Contributors.objects.create(role=validated_data['role'],
                                             permission=validated_data['permission'],
                                             user_id=validated_data['user'].id, project_id=int(id))

        contri.save()
        return contri


# Issues Serializer
class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = ('id', 'title', 'desc', 'tag', 'priority', 'status', 'assignee', 'project', 'author')

    def create(self, validated_data):
        id = self.context.get('view').kwargs.get('project_pk')

        issue = Issues.objects.create(title=validated_data['title'], desc=validated_data['desc'],
                                      priority=validated_data['priority'], status=validated_data['status'],
                                      tag=validated_data['tag'], author_id=self.context['request'].user.id,
                                      assignee_id=validated_data['assignee'].id, project_id=int(id))
        issue.save()
        return issue


# Comments
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'description', 'author', 'issue')

    def create(self, validated_data):
        id = self.context.get('view').kwargs.get('issue_pk')
        comment = Comments.objects.create(description=validated_data['description'], author=self.context['request'].user, issue_id=id)

        comment.save()
        return comment
