from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

from .forms import UserForm, UserProfileInfoForm


def index(request):
    return render(request, 'index.html')


@csrf_protect
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'lname' in request.POST:
                print('found it')
                profile.lname = request.POST['lname']
                profile.name = request.POST['username']
                profile.email = request.POST['email']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'registration.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


@csrf_protect
def user_login(request):
    error ={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('sultan'))
            else:
                return HttpResponse('Ваш аккаунт не активный')
        else:
            error['error_login'] = 'Вы ввели неверные данные'
            return render(request, 'index_login.html',{'error_login':error['error_login']})
            # return HttpResponseRedirect(reverse('user_login'))
    else:
        return render(request, 'index_login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
