from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = "__all__"

	def validate_username(self, value):
		user = User.objects.filter(username=value)
		if user.exists():
			raise serializers.ValidationError('User already exists!')
		return value


	def validate_password2(self, value):
		if validated_data['password'] != value:
			raise serializers.ValidationError('First and second passwords are not the same')
		return value


	# validations must be tested, also the login process and task update, delete processes!