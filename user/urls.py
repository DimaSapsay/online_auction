from django.urls import path

from .views import index, singup

app_name = 'user'

urlpatterns = [
    path('', index, name='index'),
    path('singup', singup, name='singup')
]