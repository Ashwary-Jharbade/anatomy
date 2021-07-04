from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	mobile = models.CharField(max_length=10)
	def __str__(self):
		return self.mobile

class SequenceTest(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	file = models.FileField(upload_to='datafolder',blank=True)

class TestHistory(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	sfile = models.ForeignKey(SequenceTest,on_delete=models.CASCADE)
	result = models.CharField(max_length=10)
	sequenceid = models.CharField(max_length=20)
	sequencefeature = models.IntegerField()
	dnaseqlength = models.IntegerField()
	mrnasequencelength = models.IntegerField()
	proteinSequenceLength = models.IntegerField()
	L = models.IntegerField()
	S = models.IntegerField()
	T = models.IntegerField()
	C = models.IntegerField()
	F = models.IntegerField()
	R = models.IntegerField()
	V = models.IntegerField()
	Y = models.IntegerField()
	N = models.IntegerField()
	I = models.IntegerField()
	K = models.IntegerField()
	G = models.IntegerField()
	A = models.IntegerField()
	H = models.IntegerField()
	Q = models.IntegerField()
	P = models.IntegerField()
	D = models.IntegerField()
	E = models.IntegerField()
	W = models.IntegerField()
	M = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return "{0} ({1})".format(self.date,self.result)
