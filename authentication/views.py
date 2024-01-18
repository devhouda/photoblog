from django.shortcuts import render, redirect
from authentication import forms
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def logout_user(request):
    logout(request)
    return redirect('login')


def login_page(request):
    message = ''
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Login failed!'
    return render(request, 'authentication/login.html', context={'form': form, 'message': message})