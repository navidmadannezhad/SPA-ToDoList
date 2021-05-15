from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class Register(APIView):
	def post(self, request):
		serialized = UserSerializer(data=request.data)
		if serialized.is_valid():
			serialized.save()
			user = User.objects.get(username=request.data['username'])
			token = Token.objects.create(user=user)
			token.save()
			return Response(token.key, status=200)
		else:
			return Response(serialized.errors, status=400)



class Login(APIView):
	def post(self, request):
		serialized = UserSerializer(data=request.data)
		if serialized.is_valid():
			user = authenticate(username=request.data['username'], password=request.data['password'])
			if user is not None:
				token = Token.objects.get(user=user)
				return Response(token.key, status=200)
			else:
				return Response('unvalid credentials', status=400)
		else:
			return Response(serialized.errors, status=400)
