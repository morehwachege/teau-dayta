from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.urls.base import reverse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect(reverse('members:login_user'))


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect(reverse('members:login_user'))


def blank(request):
    return render(request, 'base.html')


def forgot_password(request):
    return render(request, 'forgot-password.html')
