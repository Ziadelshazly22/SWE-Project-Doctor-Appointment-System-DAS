from django.contrib.auth.models import AbstractUser #authentication
from django.db import models #define database fields 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
# Base User class
class User(AbstractUser):
    ROLE_CHOICES = [
        ('Patient', 'Patient'),
        ('Receptionist', 'Receptionist'),
        ('Doctor', 'Doctor'),
        ('Admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    def __str__(self):
        return f"{self.username} ({self.role})"
    
class CustomUserCreationForm(UserCreationForm): #Extends the built-in UserCreationForm to work with the custom User model.
    class Meta: #admins to create a new user account ,meta Specifies which model and fields to include in the form
        model = User
        fields = ('username', 'email', 'role', 'phone_number')

class CustomUserChangeForm(UserChangeForm): #admin can edit or update an existing user's details
    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'phone_number')
