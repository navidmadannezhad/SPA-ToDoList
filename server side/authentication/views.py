from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class Register(APIView):
	def post(self, request):
		serialized = UserRegisterSerializer(data=request.data)
		if serialized.is_valid():
			serialized.save()
			user = User.objects.get(username=request.data['username'])
			token = Token.objects.create(user=user)
			token.save()
			context = {
				'token': token.key,
				'user': user.username
			}
			return Response(context, status=200)
		else:
			return Response(serialized.errors, status=400)



class Login(APIView):
	def post(self, request):
		serialized = UserLoginSerializer(data=request.data)
		if serialized.is_valid():
			user = authenticate(username=request.data['username'], password=request.data['password'])
			if user is not None:
				token = Token.objects.get(user=user)
				context = {
					'token': token.key,
					'user': user.username
				}
				return Response(context, status=200)
			else:
				context = {
					'invalid': ['نام کاربری با پسوورد همخوانی ندارد']
				}
				return Response(context, status=400)
		else:
			return Response(serialized.errors, status=400)



class AuthenticateToken(APIView):
	def post(self, request):
		recievedToken = request.data['token']
		if(Token.objects.filter(key=recievedToken).exists()):
			return Response(True, status=200)
		else:
			return Response(False, status=400)