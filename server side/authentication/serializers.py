from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
	
	password = serializers.CharField(error_messages={'blank': 'Password is empty!'})
	password2 = serializers.CharField(error_messages={'blank': 'Password2 is fucking empty!'})
	username = serializers.CharField(error_messages={'blank': 'username is blank!'},validators=[UniqueValidator(queryset=User.objects.all(), message="Username has been used before in database!")])

	class Meta:
		model = User
		fields = '__all__'


	def create(self, validated_data):
		user = User(
			username=validated_data['username'],
			password=make_password(validated_data['password'])
		)
		user.save()
		return user


	def validate(self, data):
		if data['password'] != data['password2']:
			raise serializers.ValidationError('Passwords are not the same!')
		return data

		
		