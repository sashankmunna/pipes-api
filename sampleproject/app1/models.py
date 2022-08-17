from django.db import models

# Create your models here.
class pipes(models.Model):
	Pipe_name=models.CharField(max_length=30)
	Stock=models.IntegerField()
	Grade=models.CharField(max_length=3)
	colour=models.CharField(max_length=15)
	size=models.CharField(max_length=10)
	quality=models.CharField(max_length=20)