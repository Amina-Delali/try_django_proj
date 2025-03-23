# from rest_framework import serializers
# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login']

# class RegisterUserSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(write_only=True, max_length=200, )
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'confirm_password']
#         extra_kwargs = {'password': {'write_only': True}}
        
#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username= validated_data['username'],
#             email=validated_data['email'],
#             first_name = validated_data['first_name'],
#             last_name = validated_data['last_name'],
#             password= validated_data['password']
#         )
#         return user
    
# from django.contrib.auth.models import Group, User
# from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']

from rest_framework import serializers
from notes.models import Note
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["task", "completed", "timestamp", "updated", "user"]