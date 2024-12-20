
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Define additional fields for the custom user model
    ROLE_CHOICES = [
        ('Patient', 'Patient'),
        ('Receptionist', 'Receptionist'),
        ('Doctor', 'Doctor'),
        ('Admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Patient')
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
class Admin(User): #Admin class inherits from the User class and adds additional functionality for managing user roles.
   
    def assign_role(self, user, role):  #allows an Admin to change the role of another user.
        """Assign a role to a user."""
        if self.role == 'Admin':
            user.role = role
            user.save()
        else:
            raise PermissionError("Only Admins can assign roles.")
