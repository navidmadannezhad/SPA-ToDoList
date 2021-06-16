from django.shortcuts import get_object_or_404, render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from .serializers import TaskCompleterSerializer, TaskSerializer
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

    def post(self, request, title):
        try:
            task = Task.objects.get(title=title)
            try: 
                task.delete()
                context = {
                    'success': 'برنامه با موفقیت حذف شد'
                }
                return Response(context, status=200)
            except:
                context = {
                    'failure': 'حذف برنامه با مشکل روبرو شد'
                }
                return Response(context, status=400)
        except:
            return Response('برنامه مورد نظر یافت نشد', status=400)


# done!
class TaskUpdate(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, title):
        try:
            task = Task.objects.get(title=title)
            serializer = TaskSerializer(instance=task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response('nice!', status=200)
            return Response(serializer.errors, status=400)
        except:
            return Response('برنامه مورد نظر یافت نشد', status=400)






class TaskCompleter(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, title):
        task = get_object_or_404(Task, title=title)
        serializer = TaskCompleterSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                'completer': 'وضعیت برنامه با موفقیت تغییر کرد'
            }
            return Response(context, status=200)
        else:
            context = {
                'invalid': 'تغییر وضعیت برنامه با شکست روبرو شد'
            }
            return Response(serializer.errors, status=400)