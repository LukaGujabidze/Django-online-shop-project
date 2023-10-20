from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('cloth.html/', views.cloth, name='cloth'),
    path('toys.html/', views.toys, name='toys'),
    path('perfume.html/', views.perfume, name='perfume'),
    path('electrics.html/', views.electrics, name='electrics'),
    path('deals.html/', views.deals, name='deals'),
    path('account.html/', views.account, name='account'),
    path('contact.html/', views.contact, name='contact'),
    path('about.html/', views.about, name='about'),
    path('privacy.html/', views.privacy, name='privacy'),
    path('register.html/', views.register, name='register'),
    path('sign_in.html/', views.sign_in, name='sign_in'),
    path('cart.html/', views.cart, name='cart'),
]