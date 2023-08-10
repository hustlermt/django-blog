from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def login(request):
    template_name = 'login.html'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if not user.is_active:
                messages.error(
                    request, 'Your account has been deactivate, please contact Sketchy.')
                return render(request, template_name)
            auth.login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('accounts:redirect_logged')
        messages.error(request, 'Invalid username or password.')
    return render(request, template_name)

def redirect_logged(request):
    return redirect('blog:posts')

def user_logout(request):
    auth.logout(request)
    messages.info(request,'Logged out Successfully!')
    return redirect('/')

def register(request):
    template_name = 'register.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_user= User.objects.create_user(username=username,email=None,password=password)
        print(new_user.id) 
        print(new_user.password)
        if new_user:
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'You have successfully register an account.')
                return redirect('accounts:redirect_logged')
    return render(request, template_name)
