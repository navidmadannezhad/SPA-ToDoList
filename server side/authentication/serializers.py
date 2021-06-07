from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
	
	username = serializers.CharField(error_messages={'blank': 'لطفا نام کاربری خود را وارد کنید'}, validators=[UniqueValidator(queryset=User.objects.all(), message="نام کاربری قبلا ثبت شده است")])
	password = serializers.CharField(error_messages={'blank': 'لطفا پسوورد خود را وارد کنید'})
	password2 = serializers.CharField(error_messages={'blank': 'لطفا پسوورد خود را تکرار کنید'})

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

	def validate_password2(self, value):
		data = self.get_initial()
		if value != data['password']:
			raise serializers.ValidationError('دو رمز عبور یکسان نیستند')
		return value

	def validate(self, data):
		try:
			data['username'].encode(encoding='ascii').decode('ascii')
			data['password'].encode(encoding='ascii').decode('ascii')
			data['password2'].encode(encoding='ascii').decode('ascii')
		except UnicodeEncodeError:
			raise serializers.ValidationError('ورودی ها تنها می‌توانند شامل حروف  و اعداد انگلیسی باشند')
		return data		