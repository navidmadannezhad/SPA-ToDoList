from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
	title = models.CharField(max_length=30, null=True)
	status = models.BooleanField(default=False)
	description = models.TextField(null=True)
	user = models.ForeignKey(User, related_name="task", on_delete=models.CASCADE)

	def __str__(self):
		return self.title
