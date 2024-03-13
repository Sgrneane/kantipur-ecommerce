from django.contrib.auth import authenticate,get_user_model
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

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = None
        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                user_model = get_user_model()
                try:
                    user_instance = user_model.objects.get(email=email)
                    # If user exists but password is incorrect
                    if not user_instance.check_password(password):
                        raise serializers.ValidationError({'password': 'Incorrect password'})
                except user_model.DoesNotExist:
                    # If user does not exist
                    raise serializers.ValidationError({'email': 'User with this email does not exist'})
        else:
            raise serializers.ValidationError('Must include "email" and "password"')

        # Django's default authentication method doesn't specify if the username or password is incorrect.
        # This is a security measure to prevent enumeration attacks.
        if not user:
            raise serializers.ValidationError('Unable to log in with provided credentials.')

        attrs['user'] = user
        return attrs

class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id','full_name','email','role','phone_number']