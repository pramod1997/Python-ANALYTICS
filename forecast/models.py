# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

choices =[
	('linear','Linear'),
	('additive','Additive'),
	('multiplicative','Multiplicative'),
]
class Document(models.Model):
	seasonal_length = models.IntegerField(default=12)
	forecast_period = models.IntegerField(default=12)
	holt_w =   models.CharField(max_length=30,choices=choices,default='additive')
	document = models.FileField(upload_to='documents/')
	uploaded_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.FileField.name

### arima class
class Arima(models.Model):
	document=models.FileField(upload_to='Arima/')
	uploaded_at=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.FileField.name

### croston class : 

class Croston(models.Model):
	document=models.FileField(upload_to='Croston/')
	uploaded_at=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.FileField.name


#### fbprophet

class Fbprophet(models.Model):
	document=models.FileField(upload_to='Fbprophet/')
	uploaded_at=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.FileField.name


#### implement decompostion
class Decomposition(models.Model):
	document=models.FileField(upload_to='Fbprophet/')
	uploaded_at=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.FileField.name




