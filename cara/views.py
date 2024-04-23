from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib import messages



def cart(request):
    return render(request,'cart.html')


def home(request):
    products=Product.objects.all()
    context={'products':products }
    return render(request,'index.html',context)

def shop(request):
    products=Product.objects.all()
    #for product in products:
    #print(f"Name: {product.name}, Description: {product.description}")
    context={'products':products }
    return render(request,'shop.html',context)

def contact(request):
    
    comments=Review.objects.all()
    form=CommentForm()
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'commenter': form.cleaned_data['user_name'], 'msg': form.cleaned_data['comment']})
    return render(request, 'contact.html', {'comments': comments, 'form': form})


def singleproduct(request):
    return render(request,'single-product.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate the superuser directly
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect to a success page
            return render(request,'index.html')  # Change 'home' to the URL name of your home page
        else:
            # Return an invalid login message or handle the error
            return HttpResponse("Invalid login credentials or unauthorized access")
    else:
        return render(request, 'login.html')



def logout_user(request):
    logout(request)
    messages.success(request,("You are logged out!!"))
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists")
        else:
            # Create a new user
            user = User.objects.create_user(username=username, password=password)
            # Authenticate and login the user
            auth_login(request, user)
            # Redirect to a success page
            return render(request, 'index.html')  # Change 'index' to the URL name of your home page
    else:
        return render(request, 'signup.html')


def profile(request):
    # Fetch or create the user's profile
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        # If the form is submitted, process the data
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        # If it's a GET request, populate the form with existing profile data
        form = ProfileForm(instance=user_profile)
    
    return render(request, 'profile.html', {'form': form, 'user_profile': user_profile})