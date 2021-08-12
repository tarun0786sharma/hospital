from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .models import Blog, Appointment
from .forms import BlogForm, AppointmentForm
from .decorators import *
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import get_user_model
from .filters import CategoryFilter


# Create your views here.

@unauthenticated_user
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


@unauthenticated_user
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
    context = {'user': user, 'all_data': all_data}
    return render(request, 'index.html', context)


@admin_only
@login_required(login_url='login')
def addBlog(request):
    tasks = Blog.objects.all()
    form = BlogForm()
    user = request.user

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            form.save()

        return redirect("/")

    context = {'tasks': tasks, 'form': form}
    return render(request, 'add_blog.html', context)


def viewBlogs(request):
    blogs = Blog.objects.all()
    filters = CategoryFilter(request.GET, queryset=blogs)
    orders = filters.qs
    context = {'blogs': blogs, 'filters': filters, 'orders': orders}
    return render(request, 'view_blog.html', context)


@admin_only
def myBlogs(request):
    user = request.user
    data = Blog.objects.filter(user=user).all().order_by('-id')
    return render(request, 'my_blogs.html', {'data': data})


def fullBlog(request, pk):
    blogs = Blog.objects.get(id=pk)
    context = {'blogs': blogs, }
    return render(request, 'full_blog.html', context)


def doctorList(request):
    User = get_user_model()
    qs = User.objects.filter(groups__name__in=['doctor'])
    context = {'qs': qs, }
    return render(request, 'doctors.html', context)


def bookNew(request):
    tasks = Appointment.objects.all()
    form = AppointmentForm()
    user = request.user

    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            form.save()

        return redirect("/")

    context = {'tasks': tasks, 'form': form}
    return render(request, 'appointment.html', context)


def myAppointments(request):
    user = request.user
    User = Appointment.objects.filter(user=user)
    context = {'User': User, }
    return render(request, 'my_appointments.html', context)