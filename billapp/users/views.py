from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are able to login')
            return redirect('login')
    else :
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})



def home(request):
    return render(request, 'users/home.html')
