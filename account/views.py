from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from account.forms import CreateUserForm


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {'page_name': 'LOGIN'}
    return render(request, 'account/login.html', context)


def registerPage(request):
    user = CreateUserForm()
    if request.method == 'POST':
        user = CreateUserForm(request.POST)
        group_request = request.POST.getlist('check_box_list', '')
        if user.is_valid():
            user = user.save(commit=False)
            for g in group_request:
                user.save()
                group = Group.objects.get(name=g)
                print(group)
                user.groups.add(group)
            return redirect('login')
    context = {'user': user, 'page_name': 'REGISTER ACCOUNT'}
    return render(request, 'account/register.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')
