from django.shortcuts import render, redirect, session
from .models import User


# Create your views here.
def index(request):
	return render(request, 'quoter/index.html')
def register(request):
	User.objects.validate_reg(request)
	print(result)
	if result[0] == False:
		for message in result[1]:
			messages.add_message(request, messages.ERROR, message)
		return redirect('/')
def login(request):
	result=User.objects.validate_login(request)
	if result[0] == False:
		for message in result[1]:
			messages.add_message(request, messages.ERROR, message)
		return redirect('/')
	else:
		request.session.user_id = result[1].id 
		request.session.email = result[1].email
		return redirect('/add')
def add(request):
	pass
def profile(request):
	return render(request,'quoter/profile.html')