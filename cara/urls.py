from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    path('',views.home,name='index'),
    path('index',views.home,name='index'),
    path('shop', views.shop, name='shop'),
    path('contact', views.contact, name='contact'),
    path('single-product', views.singleproduct, name='single-product'),
    path('login', views.login, name='login'),
    path('cart', views.cart, name='cart'),
    path('signup',views.signup,name='signup'),
    path('logout', views.logout_user, name='logout'),
    path('profile',views.profile,name='profile')

    
]

