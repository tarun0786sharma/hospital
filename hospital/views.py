from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import get_user_model


# Create your views here.


def registerPage(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')
            return render(request, 'login.html')

    context = {}
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required(login_url='login')
def home(request):
    user = request.user
    User = get_user_model()
    all_data = User.objects.all()
    print(user.first_name)
    context = {'user': user, 'all_data': all_data}
    return render(request, 'index.html', context)
