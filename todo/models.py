from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=30)
	user = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Task(models.Model):
	created_time = models.DateTimeField(auto_now=True)
	updated_time = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=128)
	content = models.CharField(max_length=3000)
	status = models.BooleanField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
