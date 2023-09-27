from django.shortcuts import render,redirect


def auth_customer(function):
    def wrapper(request,args,*kwargs):
        if 'Customer' in request.session:
            return function(request,args,*kwargs)
        else:
            return redirect('common:cust_login')
    
    return wrapper