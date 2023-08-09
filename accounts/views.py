import requests

from django.shortcuts import render,redirect
# from .forms import Registration
from django.contrib import auth
from django.contrib import messages
from django.urls import reverse
# Create your views here.


def register(request):

	return render (request, 'register.html')

def login(request):
    template_name = 'login.html'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if not user.is_active:
                messages.error(
                    request, 'Your account has been deactivated.')
                return render(request, template_name)
            auth.login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect(reverse('accounts:redirect_logged'))
        messages.error(request, 'Invalid username or password.')
    print("port number")
    print(request.META['SERVER_PORT']) 
    return render(request, template_name)


