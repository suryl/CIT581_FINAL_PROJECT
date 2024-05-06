from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def cart(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if the user is not authenticated
    try:
        cart = Cart.objects.get(user=request.user)  # Ensure the user has a cart
        items = cart.cartitem_set.all()  # Retrieve all items from the user's cart
    except Cart.DoesNotExist:
        items = []  # If no cart exists, show an empty list
    return render(request, 'cart.html', {'cart_items': items})

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)

def shop(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop.html', context)

def contact(request):
    comments = Review.objects.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'commenter': form.cleaned_data['user_name'], 'msg': form.cleaned_data['comment']})
    return render(request, 'contact.html', {'comments': comments, 'form': form})

def singleproduct(request):
    return render(request, 'single-product.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return render(request, 'index.html')
        else:
            return HttpResponse("Invalid login credentials or unauthorized access")
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("You are logged out!!"))
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists")
        else:
            user = User.objects.create_user(username=username, password=password)
            auth_login(request, user)
            return render(request, 'index.html')
    else:
        return render(request, 'signup.html')

def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)
    return render(request, 'profile.html', {'form': form, 'user_profile': user_profile})


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')  # Adjust the redirect to wherever you'd like the user to go after adding an item

@login_required
def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

