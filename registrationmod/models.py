import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone

class Register(models.Model):
	username = models.CharField(max_length=30)
	gender = models.CharField(max_length=10)
	dob = models.DateField()
	patientid = models.FloatField(default=0)
	address = models.TextField()
	phoneno = models.IntegerField()
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.patientid


class Appointment(models.Model):
	
	patientid = models.ForeignKey(Register,on_delete=models.CASCADE)
	department = models.TextField()
	date = models.DateField()

	def __str__(self):
		return str(self.patientid)
'''
	def get_absolute_url(self):
        return reverse('NewAppt',kwargs={'pk':self.purch_id})
'''
