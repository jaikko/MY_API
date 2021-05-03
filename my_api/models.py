from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_staff= None
    is_superuser= None
    username= None
    last_login= None
    email = models.EmailField(max_length=70, blank=False, unique= True)
    password = models.CharField(max_length=100, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'first_name']
    
    
class Projects(models.Model):
    CHOICES = (
        ('back-end','back-end'),
        ('front-end','front-end'),
        ('IOS','IOS'),
        ('Android','Android'),
    )
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    type = models.CharField(max_length=300, choices = CHOICES)
    
class Contributors(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='contributors', null=True)
    role = models.CharField(max_length=300)
    permission =  models.CharField(max_length=300)
    
class Issues(models.Model):
    tag_choice = (
        ('bug','bug'),
        ('amélioration','amélioration'),
        ('tâche','tâche'), 
    )
    
    status_choice = (
        ('A faire', 'A faire'),
        ('En Cours', 'En cours'),
        ('Terminé', 'Terminé')
    )
    
    priority_choice = (
        ('Faible', 'Faible'),
        ('Moyenne', 'Moyenne'),
        ('Elevée', 'Elevée')
    )
    
    title = models.CharField(max_length=300)
    desc = models.CharField(max_length=300)
    tag = models.CharField(max_length=300, choices = tag_choice)
    priority = models.CharField(max_length=300, choices = priority_choice)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, blank=True, null=True, related_name="issues_project")
    status = models.CharField(max_length=300, choices = status_choice)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues_author', null=True)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='assignee')
    time_created = models.DateTimeField(auto_now_add=True)
    
class Comments(models.Model):

    description = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_author', null=True)
    issue = models.ForeignKey(Issues, on_delete=models.CASCADE, related_name='comments', null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    
    
    
    
    
