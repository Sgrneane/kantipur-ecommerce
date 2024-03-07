from django.shortcuts import render
from django.contrib.auth import get_user_model,authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.views import LoginView
from .serializers import CreateUserSerializer,CustomLoginSerializer,ListUserSerializer
from .models import CustomUser
# Create your views here.

class UserViewsets(viewsets.ModelViewSet):
    queryset=get_user_model().objects.all()
    serializer_class= ListUserSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CreateUserSerializer
        else:
            return super().get_serializer_class()
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Save the new object to the database
        self.perform_create(serializer) #task 1

        # Create a custom response
        response_data = {
            "message": "Your account has been created successfully",
            "data": ListUserSerializer(serializer.instance).data
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    


#Custom login view created overriding dj-rest-auth     
class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer