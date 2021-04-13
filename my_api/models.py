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
    
    author = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=True)
    description = models.CharField(max_length=300, blank=True)
    type = models.CharField(max_length=300, choices = CHOICES, blank=True)
    
class Contributors(models.Model):
 
    user = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='projects')
    role = models.CharField(max_length=300)
    permission =  models.CharField(max_length=300)
    
