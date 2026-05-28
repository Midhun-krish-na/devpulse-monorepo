from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Creating custom user and superuser as we set username=None in our User model
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role','MANAGER')

        if extra_fields.get('is_staff') is not False:
            pass

        if extra_fields.get('is_superuser') is not False:
            pass

        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):
    # Role choices
    ROLE_CHOICES = (
        ('MANAGER', 'Manager'),
        ('DEVELOPER', 'Developer'),
    )

    # Remove username and use email for authentication
    username = None
    email = models.EmailField(unique=True)

    # User role field
    role = models.CharField(
        max_length=15,
        choices=ROLE_CHOICES,
        default='DEVELOPER'
    )

    # Link our brand new custom manager to this model
    objects = UserManager()

    # Set email as the login field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} ({self.role})"