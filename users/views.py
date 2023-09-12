from django.contrib.auth import authenticate, login, logout

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# from .models import User

from .serializer import UserSerializer, UserLoginSerializer

class RegisterUser(APIView):  
  def post(self, request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      # print(request.data)
      # print(serializer.validated_data)
      # user = serializer.validated_data['user']
      user = serializer.save()
      login(request, user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
  def post(self, request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.validated_data
      login(request, user)
      # print(serializer.validated_data)
      return Response({'message': 'Logged in successfully'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class UserLogout(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request):
    logout(request)
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)


# class UsersProfile(APIView):
#   # get user with id
#   def get_user_by_id(self, id):
#     try:
#       return User.objects.get(id=id)
#     except User.DoesNotExist:
#       return None

#   def get(self, request, id):
#     user = self.get_user_by_id(id)
#     serializer = UserSerializer(user)
#     if user is not None:
#       return Response(serializer.data)
#     return Response(status=status.HTTP_404_NOT_FOUND)
  
#   def put(self, request, id):
#     user = self.get_user_by_id(id)
#     serializer = UserSerializer(user, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
#   def delete(self, request, id):
#     user = self.get_user_by_id(id)
#     if user is not None:
#       user.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)
#     return Response(status=status.HTTP_404_NOT_FOUND)
 