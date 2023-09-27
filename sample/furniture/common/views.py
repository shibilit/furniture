from django.db.models.functions import Random
from random import sample
from django.conf import settings
from django.shortcuts import redirect, render
from common.decorators import auth_customer

from common.models import Customer, Seller
from django.core.mail import send_mail
from django.conf import settings
from customer.models import CustomCart

from seller.models import Product

# Create your views here.
def home(request):
    all_product = Product.objects.order_by(Random())
    setlimit = sample(list(all_product),8)

    context = {
        'data' : setlimit
        

    }
    return render(request, 'common/home.html',context)
# @auth_customer
def prod_list(request,id):
    view_product=Product.objects.get(id=id)

    if request.method == 'POST':
        prod_id=Product.objects.get(id=id)
        cust_id=Customer.objects.get(id = request.session['Customer'])
        qty=request.POST['qty']
        
        add_cart = CustomCart(
            product=prod_id,
            customer=cust_id,
            quantity=qty
        )
        add_cart.save()

    return render(request, 'common/prod_list.html',{'data':view_product})

def abuot(request):
    return render(request, 'common/about.html')
def cust_login(request):
    msg = ''
    if request.method =='POST':
        customer_mail=request.POST['c_mail']
        customer_pass=request.POST['c_pass']
        try:
            find_customer = Customer.objects.get(e_mail=customer_mail,password=customer_pass)
            request.session['Customer'] = find_customer.id
            return redirect('customer:home')
        except:
            msg = 'E-mail or Password Invalid'

    return render(request, 'common/cust_login.html',{'msg':msg})

def cust_reg(request):
    if request.method == "POST":
        cust_name=request.POST['c_name']
        cust_geder=request.POST['c_gender']
        phone=request.POST['c_number']
        cust_address=request.POST['c_address']
        cust_mail=request.POST['c_mail']
        cust_password=request.POST['c_pass']
        cust_cnfm_pass=request.POST['c_confirm pass']
        cust_img=request.FILES['c_image']


        new_customer = Customer(
            name=cust_name,
            gender=cust_geder,
            phone=phone,
            address=cust_address,
            e_mail=cust_mail,
            password=cust_password,
            cnfm_password=cust_cnfm_pass,
            image=cust_img

        )

        new_customer.save()
     
    return render(request, 'common/cust_reg.html')

def seller_login(request):
    msg=''
    if request.method == 'POST':
        seller_username= request.POST['seller_name']
        seller_password= request.POST['seller_pass']
        try:
            find_seller = Seller.objects.get(username=seller_username,password=seller_password)
            request.session['Seller'] = find_seller.id
            return redirect('seller:home')
        except:
            msg = 'username or password is not invalid'
            
    
    return render(request, 'common/seller_login.html',{'msg':msg})

def seller_reg(request):
    if request.method == 'POST':
        seller_name = request.POST['s_name']
        seller_company_name = request.POST['s_company name']
        seller_gender = request.POST['s_gender']
        seller_bank_name = request.POST['s_bank_name']
        seller_eamil = request.POST['s_email']
        seller_cmpny_address = request.POST['s_company_address']
        seller_number = request.POST['s_num']
        seller_acc_holder_name = request.POST['s_account_holder_name']
        seller_address = request.POST['s_address']
        seller_ac_nubmer = request.POST['s_ac_number']
        seller_image = request.FILES['s_image']
        seller_ifsc =request.POST['s_ifsc']

        new_seller = Seller(
            name=seller_name,
            company_name=seller_company_name,
            gender = seller_gender,
            bank_name = seller_bank_name,
            e_mail = seller_eamil,
            company_address = seller_cmpny_address,
            phone = seller_number,
            acc_holder = seller_acc_holder_name,
            address = seller_address,
            accNo = seller_ac_nubmer,
            image = seller_image,
            ifsc =seller_ifsc
        )
        new_seller.save()

    return render(request, 'common/seller_reg.html')



def seller_forgot(request):
     msg =''
     if request.method=='POST':
        entered_email = request.POST['forget_mail']
        try:
            check=Seller.objects.get(e_mail = entered_email)
            password=check.password
            send_mail(
                'your password is',
                password,
                settings.EMAIL_HOST_USER,
                [entered_email],
                fail_silently = False
            )
            msg='your password is sand to your mail check it now'
        except:
            msg = 'enter registered email'
     return render(request, 'common/seller_forgot.html', {'msg': msg})

def cust_forgot(request):
    msg =''
    if request.method=='POST':
        entered_email = request.POST['forget_mail']
        try:
            check=Customer.objects.get(e_mail = entered_email)
            password=check.password
            send_mail(
                'your password is',
                password,
                settings.EMAIL_HOST_USER,
                [entered_email],
                fail_silently = False
            )
            msg='your password is sand to your mail check it now'
        except:
            msg = 'enter registered email'
    return render(request, 'common/cust_forgot.html', {'msg': msg})



