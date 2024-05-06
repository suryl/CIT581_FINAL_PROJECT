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
    path('signup',views.signup,name='signup'),
    path('logout', views.logout_user, name='logout'),
    path('profile',views.profile,name='profile'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove-from-cart'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

]

