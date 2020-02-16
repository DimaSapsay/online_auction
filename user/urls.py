from django.urls import path

from .views import index, singup, singin, logout_view, account, edit_account

app_name = 'user'

urlpatterns = [
    path('', index, name='index'),
    path('singup', singup, name='singup'),
    path('singin', singin, name='singin'),
    path('logout_view', logout_view, name='logout_view'),
    path('account', account, name='account'),
    path('edit-account', edit_account, name='edit_account'),
]

