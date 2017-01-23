from rest_framework import serializers
from .models import Task, User
from django.contrib.auth import get_user_model

class TaskSerializer(serializers.ModelSerializer):

     image = serializers.ImageField(max_length=None,use_url=True)
     doc = serializers.FileField(max_length=None,use_url=True)
     
     class Meta:
         model = Task
         fields = ('id','task_name','task_desc','completed','date_created','image','doc')

class UserSerializer(serializers.ModelSerializer):
     first_name = serializers.CharField(max_length=20)
     last_name = serializers.CharField(max_length=20)
     email = serializers.CharField(max_length=20)
     username =serializers.CharField(max_length=20)
     password = serializers.CharField(write_only=True)




     def create(self, validated_data):
         user = get_user_model().objects.create(username = validated_data['username'])
         user.set_password(validated_data['password'])
         user.save()
         return user

     class Meta:
         model = User
         fields = ('first_name','last_name','email','username','password')



