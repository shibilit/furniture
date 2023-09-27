from django.urls import path
from .import views
app_name = 'customer'
urlpatterns=[
     path('home',views.home, name="home"),
     path('help',views.help, name="help"),
     path('cart',views.cart, name="cart"),
     path('product_dtls/<int:id>',views.product_dtls, name="product_dtls"),
     path('product/<int:id>',views.product, name="product"),
     path('master',views.master, name="master"),
     path('myorders',views.myorders, name="myorders"),
     path('remove/<int:id>', views.remove, name='remove'),
     path('cust_logout',views.cust_logout, name='cust_logout'),
     path('account',views.account, name='account'),
     path('about',views.about, name='about'),
     path('checkout',views.checkout, name='checkout'),
     path('payment',views.payment, name='payment'),
     path('result',views.result, name='result'),


]     