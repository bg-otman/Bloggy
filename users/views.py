from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def register_user(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("users:login")
	else:
		form = UserCreationForm()
	return render(request, 'users/register.html', { 'form' : form })

def login_user(request):
	next_url = request.GET.get('next') or request.POST.get('next')
	error_msg = None
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			if next_url != 'None':
				return redirect(next_url)
			else:
				return redirect('posts:list')
		else:
			error_msg = "Invalid UserName or Password, Please Try again!"
	return render(request, 'users/login.html', { 'next': next_url, 'error_msg' : error_msg })

def logout_user(request):
	if request.method == "POST":
		logout(request)
		return redirect("users:login")
