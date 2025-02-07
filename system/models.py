from django.db import models
class StudentDetails(models.Model):
	fullname=models.CharField(max_length=100,default="")
	contactnumber=models.CharField(max_length=15,default="")
	address=models.CharField(max_length=100,default="")
	gender=models.CharField(max_length=20,default="")
	dateofbirth=models.CharField(max_length=20,default="")
	qualification=models.CharField(max_length=10,default="")
	username=models.CharField(max_length=10,default="")
	password=models.CharField(max_length=10,default="")

class tolldetails(models.Model):
	state=models.CharField(max_length=10,default="")
	nhnumber=models.CharField(max_length=10,default="")
	vehicletype=models.CharField(max_length=10,default="")
	vehiclenumber=models.CharField(max_length=10,default="")
	selectplan=models.CharField(max_length=10,default="")
	contactnumber=models.CharField(max_length=10,default="")

class paydetails(models.Model):
	cardaccepted=models.CharField(max_length=10,default="")
	nameoncard=models.CharField(max_length=10,default="")
	cardnumber=models.CharField(max_length=10,default="")
	amount=models.CharField(max_length=10,default="")


# Create your models here.
