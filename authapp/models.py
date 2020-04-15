from django.db import models

# Create your models here.
class inVoice(models.Model):
	statuss=(('sent','sent'),('recieved','recieved'),('created','created'))
	ponumber = models.BigIntegerField()
	name = models.CharField (max_length=50)
	personName = models.CharField(max_length=50)
	phoneNumber = models.BigIntegerField()
	email = models.EmailField()
	address = models.TextField()
	status = models.CharField(max_length=50,null=True,choices=statuss)

	def __str__(self):
		return self.personName