from django.db import models
from django.utils import timezone

class Register(models.Model):
	name = models.ForeignKey('auth.User')
	gender = models.CharField(max_length=100)
	dob = models.DateField()
	patientid = models.AutoField( primary_key=True)
	adress = models.TextField()
	telephone = models.FloatField()
	mobile = models.FloatField()

	def __str__(self):
		return self.patientid
