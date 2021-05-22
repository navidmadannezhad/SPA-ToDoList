from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
	
	password2 = serializers.CharField()

	class Meta:
		model = User
		fields = '__all__'
		extra_kwargs = {
			'username':{
				'validators':[
					UniqueValidator(queryset=User.objects.all(), message="نام کاربری قبلا ثبت شده!")
				],
				'error_messages':{
					'blank': 'لطفا نام کاربریت رو وارد کن',
				}
			},
			'password':{
				'error_messages':{
					'blank': 'لطفا رمز عبورت رو وارد کن'
				}
			},
			'password2':{
				'error_messages':{
					'blank': 'لطفا رمز عبور دوم رو وارد کن'
				}
			},
		}

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
		
		