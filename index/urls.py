from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name= 'home_page'),
    path('cart/', views.cart, name= 'cart_page'),
    path('category/<category>', views.filter, name= 'filter'),
    path('signup/', views.signup, name= 'signup'),
    path('login/', views.login, name= 'login'),
    path('lgout/', views.lgout, name= 'lgout'),

    path('handlepayment/', HandelRequestView.as_view(), name= 'handlepayment'),
    path('paymentverification/', views.VerificationView, name= 'paymentverification'),

    path('product/<id>', ProductDetailView.as_view(), name= 'product'),
    path('add-to-cart-<id>/', AddToCartView.as_view(), name= 'addtocart'),
    path('mycart/', MyCart.as_view(), name= 'mycart'),
    path('manage-cart/<id>', ManageCart.as_view(), name= 'Managecart'),
    path('empty/', EmptyCart.as_view(), name= 'empty'),
    path('ordernow/', OrderNow.as_view(), name= 'ordernow'),
    path('profile/', ProfileView.as_view(), name= 'profile'),
    path('search/', SearchView.as_view(), name= 'search'),
]
