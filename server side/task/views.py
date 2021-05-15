from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import TaskSerializer
from task.models import Task
from rest_framework.response import Response
from django.contrib.auth.models import User


class TaskList(APIView):
	def get(self, request):
		tasks = Task.objects.all()
		serialized = TaskSerializer(tasks, many=True)
		return Response(serialized.data, status=200)


class TaskCreate(APIView):
	def post(self, request):
		serialized = TaskSerializer(data=request.data)

		if serialized.is_valid():
			user = User.objects.get(username=request.user.username)
			serialized.save(user=user)
			return Response('Succssed!', status=200)
		else:
			return Response(serialized.errors, stats=400)


class TaskDelete(APIView):
	pass



class TaskUpdate(APIView):
	pass