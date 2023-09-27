from django.db.models.functions import Random
from django.shortcuts import redirect, render
from common.models import Customer
from customer.models import CustomCart
from django.db.models import F
from random import sample

from seller.models import Product

# Create your views here.
def home(request):
    customer=Customer.objects.get(id=request.session['Customer'])
    all_product = Product.objects.order_by(Random())
    setlimit = sample(list(all_product),12)
    context = {
        'data' : setlimit,
        'user':customer

    }
    return render(request, 'customer/home.html',context)

def cart(request):
    customer=Customer.objects.get(id=request.session['Customer'])

    cart_data = CustomCart.objects.filter(customer_id=request.session['Customer']).annotate(total=F('product__pro_price')*F('quantity'))
    grand_total = 0
  
    for i in cart_data:
        grand_total += i.total

    context = {
        'data': cart_data,
        'grand_total': grand_total,
        'user':customer
    }
    return render(request, 'customer/cart.html',context)

def product_dtls(request,id):
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

    return render(request, 'customer/product_dtls.html',{'data':view_product})

def product(request,id):
    customer=Customer.objects.get(id=request.session['Customer'])
    
    fillter = Product.objects.filter(pro_category__id=id)

    return render(request, 'customer/product.html',{'data':fillter,'user':customer})

def master(request):
    customer=Customer.objects.get(id=request.session['Customer'])
    return render(request, 'customer/master.html',{'user':customer})

def myorders(request):
    return render(request, 'customer/myorders.html')

def checkout(request):
    return render(request, 'customer/checkout.html')

def payment(request):
    return render(request, 'customer/payment.html')

def result(request):
    return render(request, 'customer/result.html')

def about(request):
    customer=Customer.objects.get(id=request.session['Customer'])

    return render(request, 'customer/about.html',{'user':customer})

def account(request):
    customer=Customer.objects.get(id=request.session['Customer'])
    if request.method == 'POST':
        up_name = request.POST['ed_name']
        up_phone = request.POST['ed_phone']
        up_email = request.POST['ed_email']
        up_gender = request.POST['ed_gender']
        up_address = request.POST['ed_address']

        edit_customer = Customer.objects.filter(id=request.session['Customer'])

        if (up_name != ''):
            edit_customer.update(name=up_name)
        else:
            print('else')
        if (up_phone != ''):
            edit_customer.update(phone=up_phone)
        else:
            print('else')
         
        if (up_email != ''):
            edit_customer.update(e_mail=up_email)
        else:
            print('else')
        if (up_gender != ''):
            edit_customer.update(gender=up_gender)
        else:
            print('else')
        if (up_address != ''):
            edit_customer.update(address=up_address)
        else:
            print('else')
        try:
            up_image = request.FILES['ed_image']
            customer.image = up_image
            customer.save()
        except:
            up_image = None
    return render(request, 'customer/account.html',{'user':customer})


def help(request):
    customer=Customer.objects.get(id=request.session['Customer'])
    
    return render(request, 'customer/help.html',{'user':customer})

def remove(request, id):
    remove_data = CustomCart.objects.filter(product_id=id)
    remove_data.delete()
    return redirect('customer:cart')

def cust_logout(request):
    del request.session['Customer']
    request.session.flush()
    return redirect('common:home')




   