from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

class UserManager(models.Model):
	def validate_reg(request):
		errors =[]
		if len(request.POST['name']) ==0:
			errors.append('Please fill in your name')
		if len(request.POST['alias']) ==0:
			errors.append('Please fill in you Alias')
		if len(request.POST['email']) ==0:
			errors.append('Please fill in your email address')
		if len(request.POST['pword']) ==0:
			errors.append('Please enter a Password')
		if len(request.POST['cpword']) ==0:
			errors.append('Please confirm your password')
		if request.POST['pword'] != request.POST['cpword']:
			errors.append('Your passwords do not match')
		if len(errors) >0:
			return(False, errors)
		else:
			user = self.create(name=request.POSt['name'], alias=request.POST['alias'], email=request.POST['email'], pword=request.POST['pword'])

	def validate_login(self, request):
		errors =[]
		if len(request.POST['email']) ==0:
			errors.append('Please Enter a Valid Email')
		if len(request.POST['pword']) ==0:
			errors.append('Please enter a password')
		if len(errors) > 0:
			return(False, errors)
class User(models.Model):
	name= models.CharField(max_length=255)
	alias= models.CharField(max_length=255)
	email= models.CharField(max_length=255)
	pword= models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

class Quote(models.Model):
	quote= models.TextField()
	user= models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)