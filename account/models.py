from django.db import models

# Create your models here.
class UserContactModel(models.Model):
	name = models.CharField(max_length=200)
	phone = models.IntegerField()
	email = models.EmailField(max_length=100)
	description = models.TextField()
