from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from .serializers import TaskSerializer
from task.models import Task
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#done!
class TaskList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.all()
        serialized = TaskSerializer(tasks, many=True)
        return Response(serialized.data, status=200)


# done!
class TaskCreate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serialized = TaskSerializer(data=request.data)

        if serialized.is_valid():
            user = User.objects.get(username=request.user.username)
            serialized.save(user=user)
            return Response('Succssed!', status=200)
        else:
            return Response(serialized.errors, stats=400)


# done!
class TaskDelete(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        try:
            task = Task.objects.get(id=id)
            try: 
                task.delete()
                return Response('task deleted!', status=200)
            except:
                return Response(serializer.errors, status=400)
        except:
            return Response('برنامه مورد نظر یافت نشد', status=400)


# done!
class TaskUpdate(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        try:
            task = Task.objects.get(id=id)
            serializer = TaskSerializer(instance=task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response('nice!', status=200)
            return Response(serializer.errors, status=400)
        except:
            return Response('برنامه مورد نظر یافت نشد', status=400)