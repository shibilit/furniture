from django.urls import path
from .import views
app_name = 'seller'
urlpatterns=[
     path('home',views.home, name="home"),
     path('help',views.help, name="help"),
     path('about',views.about, name="about"),
     path('master',views.master, name="master"),
     path('add_product',views.add_product, name="add_product"),
     path('stock/<int:stock_id>/update/', views.update_stock, name='update_stock'),
     path('get_data',views.get_data, name="get_data"),
     path('seller_logout',views.seller_logout, name='seller_logout'),
     path('account',views.account, name="account"),
     path('success',views.success, name="success"),

     # path('view_orders',views.view_orders, name="view_orders"),
]     