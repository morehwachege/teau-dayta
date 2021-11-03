from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import SignUpForm



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = request.user

            return redirect(reverse_lazy('data:index'))

        else:
            messages.success(request, 'Error logging in, please Try Again...')
            return redirect(reverse('members:login_user'))
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('members:login_user')


def login_admin(request):
    url = 'admin'
    if request.user.is_staff:
        return redirect(url)
    else:
        messages.success(request, 'Error, you\'re not an admin!')



def register_request(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()           
            return redirect(reverse('members:login_user'))
    form = SignUpForm()
    context = {
        'register_form': form
    }
    return render(request, 'authenticate/register.html', context)

        

# Create your views here.
