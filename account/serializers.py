from django.contrib.auth import get_user_model
from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth.hashers import make_password
from .models import CustomUser

#Serializer for creating user
class CreateUserSerializer(serializers.ModelSerializer):
    def validate_password(self,value):#field level validation
        if len(value) < 5:
            raise serializers.ValidationError('Password must be 5 digit')
        return make_password(value)
    

    class Meta:
        model = get_user_model()
        fields=['id','full_name','email','phone_number','role','password']


#Serializer for listing users
class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields=['id','full_name','email','phone_number','role']



class CustomLoginSerializer(LoginSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username')

class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id','full_name','email','role','phone_number']