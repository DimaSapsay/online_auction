from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import SingupForm, AccountForm, SinginForm


def index(request):
    return render(request, 'user/index.html')


def singup(request):
    singup_form = SingupForm()
    account_form = AccountForm()
    if request.method == 'POST':
        singup_form = SingupForm(request.POST)
        account_form = AccountForm(request.POST)
        if singup_form.is_valid() and account_form.is_valid():
            user = singup_form.save()
            account = account_form.save(commit=False)
            account.user = user
            account.save()
            messages.success(request, 'successful create new user')
            return redirect(reverse('user:index'))
    return render(request, 'user/singup.html', {
        'singup_form': singup_form,
        'account_form': account_form,
    })


def singin(request):
    form = SinginForm()
    if request.method == 'POST':
        form = SinginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user = authenticate(request, username=user_name, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Success! Sing in')
                return redirect(reverse('user:index'))
            else:
                messages.error(request, 'Invalid username or password!')
        else:
            messages.error(request, 'Invalit input!')
    return render(request, 'user/singin.html', {
        'form': form,
    })


def logout_view(request):
    logout(request)
    return redirect(reverse('user:index'))
