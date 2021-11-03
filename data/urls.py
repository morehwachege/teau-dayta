from django.urls import path
from .views import blank, forgot_password, index, profile

app_name = "data"

urlpatterns =[
    path('dashboard/', index, name='index'),
    path('profile', profile, name='profile'),
    path('blank', blank, name='blank'),
    path('forgot-password', forgot_password, name='forgot-password'),
]