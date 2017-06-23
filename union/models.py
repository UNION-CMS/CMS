from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

	class Meta(AbstractUser.Meta):
		pass


class Union(models.Model):
	user = models.ForeignKey(User, default=1)
	name = models.CharField(max_length=100, unique=True)
	logo = models.FileField()
	created_time = models.DateTimeField(auto_now=True)
	info = models.TextField(blank=True)

	def __unicode__(self):
		return self.name


SEX_CHOICES = (
	('M','man'),
	('W','women'),
)

POSITION_CHOICES = (
	('president', 'president'),
	('member', 'member'),
)

class Member(models.Model):
	union = models.ForeignKey(Union, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	member_id = models.IntegerField(unique=True)
	major = models.CharField(max_length=50)
	sex = models.CharField(max_length=10, choices=SEX_CHOICES)
	position = models.CharField(max_length=10, choices=POSITION_CHOICES)
	add_time = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return str(self.member_id) + '-' + self.name