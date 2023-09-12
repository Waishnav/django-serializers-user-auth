from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate, login, logout

# User = get_user_model()

class UserSerializer(serializers.Serializer):
  email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
  password = serializers.CharField(min_length=8, write_only=True)
  
  class Meta:
    model = User
    fields = "email", "password"

  def create(self, validated_data):
    user = User.objects.create_user(validated_data['email'], validated_data['password'])
    return user
  

class UserLoginSerializer(serializers.Serializer):
  email = serializers.EmailField(required=True)
  password = serializers.CharField(required=True)

  class Meta:
    model = User
    fields = "email", "password"

  def validate(self, data):
    user = User.objects.get(email=data['email'])
    password = data['password']

    if not user:
      raise serializers.ValidationError("Invalid email")

    elif user.check_password(password):
      return user
    else:
      raise serializers.ValidationError("Invalid password")
      