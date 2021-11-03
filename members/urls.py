from django.contrib.auth.models import User
from django.urls import path
from .views import login_user, logout_user, login_admin, register_request
from data.views import index

app_name = "members"
urlpatterns =[
    path('', login_user, name='login_user'),
    path('dashboard/', index, name='index'),
    path('logout/', logout_user, name='logout_user'),
    path('login_admin', login_admin, name='login_admin'),
    path("signup", register_request, name="register")
]