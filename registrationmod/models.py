import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone

class Register(models.Model):
	name = models.CharField(max_length=20)
	gender = models.CharField(max_length=100)
	dob = models.DateField()
	
	patientid = models.AutoField( primary_key=True)
	adress = models.TextField()
	phone = models.FloatField()
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.patientid


class Appointment(models.Model):
	department = models.TextField()
	date = models.DateField()

	def __str__(self):
		return self.date

