from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
	user = serializers.StringRelatedField()

	class Meta:
		model = Task
		fields = '__all__'