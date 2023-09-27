from django.urls import path
from .import views
app_name = 'ecom_admin'
urlpatterns=[
     path('home',views.home, name="home"),
     path('master',views.master, name="master"),
     path('profile',views.profile, name="profile"),
     path('seller_list',views.seller_list, name="seller_list"),
     path('customer_list',views.customer_list, name="customer_list"),
     path('approve_seller',views.approve_seller, name="approve_seller"),
     path('category',views.category, name="category"),
     path('approve_btn/<int:seller_id>', views.approve, name = 'approve_btn'),
     path('reject_btn/<int:seller_id>', views.reject, name= 'reject_btn')

]  