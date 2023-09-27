from django.urls import path
from .import views
app_name = 'common'
urlpatterns=[
     path('home',views.home, name="home"),
     path('cust_reg',views.cust_reg, name="cust_reg"),
     path('seller_reg',views.seller_reg, name="seller_reg"),
     path('cust_login',views.cust_login, name="cust_login"),
     path('seller_login',views.seller_login, name="seller_login"),
     path('seller_forgot',views.seller_forgot, name="seller_forgot"),
     path('cust_forgot',views.cust_forgot, name="cust_forgot"),
     path('prod_list/<int:id>',views.prod_list, name="prod_list"),
     path('about',views.abuot, name="about"),

]