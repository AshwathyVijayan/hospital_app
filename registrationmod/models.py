import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone

class Register(models.Model):
	patientid = models.FloatField(primary_key=True)
	username = models.CharField(max_length=30)
	gender = models.CharField(max_length=10)
	dob = models.DateField()
	address = models.TextField()
	phoneno = models.IntegerField()
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.patientid


