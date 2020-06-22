from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import UserContactModel
# Create your views here.
def contact_register(request):
	if request.method == 'POST':
		name = request.POST['name']
		phone = request.POST['phone']
		email = request.POST['email']
		description = request.POST['description']
		user_contact = UserContactModel.objects.create(name=name,phone=phone,email=email,description=description)
		user_contact.save()
		return redirect('/')
	else:
		return render(request,'contact.html')		
def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']
		if User.objects.filter(username=username).exists():
			messages.info(request,'Username already exists')
			return redirect('registration:register')
		elif User.objects.filter(email=email).exists():
			messages.info(request,'email already exists')
			return redirect('registration:register')
		else:
			user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password2,email=email)
			user.save()
			return redirect('registration:login')
		return redirect('registration:register')
	else:
		return render(request,'register.html')	
def login(request):
	if request.method == 'POST':
		username = request.POST.get('username',False);
		password = request.POST.get('password',False);
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request,'Invalid credintial')	
			return redirect('registration:login')	
	else:
		 return render(request,'login.html')
def logout(request):
	auth.logout(request)
	return redirect('/')