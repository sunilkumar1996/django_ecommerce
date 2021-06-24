from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm

class LoginView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            form = AuthenticationForm()
            return render(request, 'user/login.html', {'form': form})
        else:
            return redirect('home')

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        print(form)
        if form.is_valid():
            email = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')


class RegisterUserView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            form = CustomUserCreationForm()
            return render(request, 'user/register.html', {'form': form})
        else:
            return redirect('home')
    
    def post(self, request):
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')