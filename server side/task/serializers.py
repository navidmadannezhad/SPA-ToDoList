from rest_framework import serializers
from task.models import Task

class TaskSerializer(serializers.ModelSerializer):
	user = serializers.StringRelatedField()

	class Meta:
		model = Task
		fields = '__all__'
		extra_kwargs = {'title': {'error_messages': {'blank': 'The title should not be blank!'}}}

	def update(self, instance, validated_data):
		instance.title = validated_data.get('title', instance.title)
		instance.description = validated_data.get('description', instance.description)
		instance.status = validated_data.get('status', instance.status)
		
		instance.save()
		return instance


# validations --
# title field - not blank / Script / Sql
# 
#
#
#
#
#
#
#
#
#
