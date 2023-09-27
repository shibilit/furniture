from random import sample
from django.shortcuts import redirect, render
from common.models import Customer, Seller
from ecom_admin.models import Category
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models.functions import Random

from django.shortcuts import get_object_or_404, render

from seller.models import Product

# Create your views here.
def home(request):
    seller=Seller.objects.get(id=request.session['Seller'])
    product = Product.objects.filter(id=request.session['Seller']).values('pro_name','pro_image','pro_price')
    
    context = {
        'data' : product,
        'user':seller,
    }
    return render(request, 'seller/home.html',context)
#

def master(request):
    seller=Seller.objects.get(id=request.session['Seller'])
    return render(request, 'seller/master.html',{'user':seller})



def add_product(request):
    seller=Seller.objects.get(id=request.session['Seller'])
    all_category=Category.objects.all()
    if request.method == 'POST':
        product_name=request.POST['p_name']
        product_number=request.POST['p_number']
        product_category=request.POST['p_category']
        product_description=request.POST['p_description']
        product_price=request.POST['p_price']
        product_quantity=request.POST['p_quantity']
        product_image=request.FILES['p_image']
        print(product_category)
        new_product = Product(
            pro_name=product_name,
            pro_number=product_number,
            pro_category_id=product_category,
            pro_description=product_description,
            pro_price=product_price,
            pro_quantity=product_quantity,
            pro_image=product_image
        )
        new_product.save()
  
        

    return render(request, 'seller/add_product.html',{'data':all_category,'user':seller})

# def update_stock(request):
#     seller=Seller.objects.get(id=request.session['Seller'])
#     all_cate=Category.objects.all()
#     context = {
#         'user' : seller,
#         'data':all_cate
#     }
    
#     return render(request, 'seller/update_stock.html',context)
# # views.py


def update_stock(request, stock_id):
    stock = get_object_or_404(Product, id=stock_id)

    if request.method == 'POST':
        # Retrieve the updated data from the form
        quantity = request.POST['quantity']
        price = request.POST['price']

        # Update the stock object
        stock.pro_quantity = quantity
        stock.pro_price = price

        # Save the changes
        stock .save()

        # Redirect to a success page or do something else
        return render(request, 'success.html')

    return render(request, 'update_stock.html', {'stock':stock})








# def view_orders(request):
#     customer=Customer.objects.all()
#     product=Product.objects.get()
#     cart=Cart.objects.get

#     return render(request, 'seller/view_orders.html')

def help(request):
    seller=Seller.objects.get(id=request.session['Seller'])
    return render(request, 'seller/help.html',{'user':seller})

def success(request):
    return render(request, 'seller/success.html')

def about(request):
    seller=Seller.objects.get(id=request.session['Seller'])
    return render(request, 'seller/about.html',{'user':seller})



def account(request):
    seller=Seller.objects.get(id=request.session['Seller'])
    if request.method == 'POST':
        up_name = request.POST['ed_name']
        up_phone = request.POST['ed_phone']
        up_email = request.POST['ed_email']
        up_gender = request.POST['ed_gender']
        up_address = request.POST['ed_address']

        edit_seller = Seller.objects.filter(id=request.session['Seller'])

        if (up_name != ''):
            edit_seller.update(name=up_name)
        else:
            print('else')
        if (up_phone != ''):
            edit_seller.update(phone=up_phone)
        else:
            print('else')
       
        if (up_email != ''):
            edit_seller.update(e_mail=up_email)
        else:
            print('else')
        if (up_gender != ''):
            edit_seller.update(gender=up_gender)
        else:
            print('else')
        if (up_address != ''):
            edit_seller.update(address=up_address)
        else:
            print('else')
        try:
            up_image = request.FILES['ed_image']
            seller.image = up_image
            seller.save()
        except:
            up_image = None
    return render(request, 'seller/account.html',{'user':seller})


def seller_logout(request):
    del request.session['Seller']
    request.session.flush()
    return redirect('common:home')


@csrf_exempt
def get_data(request):
    # if request.method == 'POST':
        print("Reached inside request")

        selected_option = request.POST['option']
        print("select",selected_option)
        data = Product.objects.filter(pro_category=selected_option)
        print("ffff",data)
        data1=[ {"id":i.id,"pro_name":i.pro_name,"pro_quantity":i.pro_quantity}for i in data]
        return JsonResponse({'pro_data': data1})
    # else:
    #     return JsonResponse({'pro_data' : 'null'})



