from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Profile
from .form import *
from .helpers import *

# Create your views here.


def logout_view(request):
    logout(request)
    return redirect('/')


def home(request):
    context = {'blogs': BlogModel.objects.all()}
    return render(request,'home.html', context)

def blog_detail(request , slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request,'blog_detail.html',context)

def see_blog(request):
    context = {}
    try:
        blog_objs = BlogModel.objects.filter(user = request.user)
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)
    return render(request , 'see_blog.html' ,context)


def add_blog(request):
    context = {'form': BlogForm}
    try:
        if request.method == "POST":
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']


            blog_obj = BlogModel.objects.create(
                user = user , title = title ,
                content = content , image = image
            )
            return redirect('add_blog')

    except Exception as e:
        print(e)

    return render(request,'add_blog.html',context)

def blog_delete(request , id):
    try:
        blog_obj = BlogModel.objects.get(id = id)

        if blog_obj.user == request.user:
            blog_obj.delete()

    except Exception as e:
        print(e)
    return redirect('/see-blog/')


def blog_update(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.get(slug = slug)

        if blog_obj.user != request.user:
            return redirect('/')

        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial=initial_dict)

        if request.method == "POST":
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']


            blog_obj = BlogModel.objects.create(
                user = user , title = title ,
                content = content , image = image
            )

        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e:
        print(e)

    return render(request,'blog_update.html' ,context)

def login_view(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request , user)
            messages.success(request,"Successfully Logged in")
            return redirect('home')

        else:
            messages.error(request , "Invalid Credentials , Please try again")
            return redirect('home')

    return render(request , 'login_view.html')


def register(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        user = User.objects.create_user(username=username, email=email , password=password)
        user.save()
        messages.success(request , "User created successfully!")
        return redirect ('home')
    else:
        return render(request,'register.html')
