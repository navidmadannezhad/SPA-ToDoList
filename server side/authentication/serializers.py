from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = "__all__"
		extra_kwargs = {
			'username':{
				'validators': ['blank']
			},
			'username':{
				'validators': ['blank']
			},
			'username':{
				'validators': ['blank']
			}
		}

	def validate_username(self, value):
		user = User.objects.filter(username=value)
		if user.exists():
			raise serializers.ValidationError('User already exists!')
		return value


	def validate_password2(self, value):
		if validated_data['password'] != value:
			raise serializers.ValidationError('First and second passwords are not the same')
		return value

	def __init__(self, *args, **kwargs):
		super(UserSerializer, self).__init__(*args, **kwargs)

		self.fields['username'].error_messages['blank'] = u'لطفا نام کاربری را فراموش نکنید'
		self.fields['password1'].error_messages['blank'] = u'رمز عبور خود را وارد کنید'


	# validations must be tested, also the login process and task update, delete processes!