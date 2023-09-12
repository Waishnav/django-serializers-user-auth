from django.contrib import admin
from django.urls import path, include
from .views import RegisterUser, UserLogin, UserLogout

urlpatterns = [
    path('users/register', RegisterUser.as_view(), name="Register User"),
    # path('users/<int:id>', UsersProfile.as_view()),
    path('users/login', UserLogin.as_view()),
    path('users/logout', UserLogout.as_view()),
]
