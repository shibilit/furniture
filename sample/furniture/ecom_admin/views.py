from django.shortcuts import render,redirect
from common.models import Customer, Seller

from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
import random
from customer.models import CustomCart

from ecom_admin.models import Category

# Create your views here.
def home(request):
    total_seller = Seller.objects.all()
    total_customer = Customer.objects.all()
    total_order = CustomCart.objects.all()
    
    context = {
        'seller_count': total_seller.count(),
        'customer_count': total_customer.count(),
        'order_count':total_order.count(),
        'seller':total_seller,
        'customer': total_customer
    }
   
    return render(request, 'ecom_admin/home.html',context)

def master(request):
    return render(request, 'ecom_admin/master.html')

def profile(request):
    return render(request, 'ecom_admin/profile.html')

def seller_list(request):
    all_seller=Seller.objects.all()

    return render(request, 'ecom_admin/seller_list.html',{'data':all_seller})

def customer_list(request):
    all_cust=Customer.objects.all()
    
    return render(request, 'ecom_admin/customer_list.html',{'data':all_cust})

def approve_seller(request):
    seller= Seller.objects.filter(status = 'pending..')
    print(seller)
    return render(request, 'ecom_admin/approve_seller.html',{'data':seller})

def category(request):
    all_cat=Category.objects.all()
    if request.method == 'POST':
        category=request.POST['a_category']
        category_description=request.POST['a_description']
        try:
            category_image=request.FILES['cate_image']
        except:
            category_image=None
        new_category = Category(
            category_name=category,
            description=category_description,
            image=category_image
        )
        new_category.save()

        return redirect('ecom_admin:category')


    return render(request, 'ecom_admin/category.html',{'data':all_cat})

# \\\\\\\\\\\\\\APPROVE THE SELLER///////////

def approve(request,seller_id):
   
    try:
        change = Seller.objects.get(id=seller_id)

        print("STATUS CHANGED")
        seller_name= change.name
        mail = change.e_mail
        username = random.randint(1111,9999)
        password = '@' + seller_name.lower() + str(username)
        message = 'Mr/Mrs' + str(seller_name) + 'welcome to our shop, your username is : ' + str(username) + ' and your password is :' + str(password)
    
        send_mail(
            'Congradualations',
            message,
            settings.EMAIL_HOST_USER,
            [mail],
            fail_silently = False

        )
        print(mail,username,password)
        change.status = 'approved'
        change.username = username
        change.password = password
        change.save()
        
    except:
        print('500 ERROR') 
   
    return redirect('ecom_admin:approve_seller')       

def reject(request,seller_id):
    seller = Seller.objects.get(id =seller_id)
    name = seller.name
    mail = seller.e_mail 

    message = 'Mr/Mrs' + name + 'sorry for the in convenience you are no eligible for our terms and conditions ELITE FURNISHING'
    send_mail(
        'REJECTED',
        message,
        settings.EMAIL_HOST_USER,
        [mail],
        fail_silently = False
    )
    seller.save()

    return redirect('ecom_admin:approve_seller')  


    

