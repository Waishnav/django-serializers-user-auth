from django.db import models

from django.contrib.auth import models as auth_models

class UserManager(auth_models.BaseUserManager):
  def create_user(self, email, password):
    if not email:
      raise ValueError('The Email must be set')
    email = self.normalize_email(email)
    user = self.model(email=email)
    user.set_password(password)
    user.save()
    return user
  
  def create_superuser(self, email, password, **extra_fields):
    superuser = self.create_user(email, password)
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.is_active = True
    superuser.save()
    return superuser
  
  
class User(auth_models.AbstractUser):
  first_name = models.CharField(max_length=255, verbose_name='First Name')
  last_name = models.CharField(max_length=255, verbose_name='Last Name')
  email = models.EmailField(unique=True, verbose_name='Email Address')
  password = models.CharField(max_length=255)
  username = None

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = UserManager()

  def __str__(self):
    return self.email

  
