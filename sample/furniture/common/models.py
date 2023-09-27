from django.db import models

# Create your models here.
class Seller(models.Model):
    name=models.CharField(max_length=50)
    company_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=50)
    bank_name=models.CharField(max_length=100)
    e_mail=models.CharField(max_length=50)
    company_address=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    acc_holder=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    accNo=models.BigIntegerField()
    image = models.ImageField(upload_to='seller/')
    ifsc=models.CharField(max_length=50)
    username=models.CharField(max_length=100,default='')
    password=models.CharField(max_length=100,default='')
    status=models.CharField(max_length=30, default='pending..')
     
    class Meta:
        db_table='seller'

class Customer(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50,default='')
    phone=models.BigIntegerField()
    address=models.CharField(max_length=200,default='')
    e_mail=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    cnfm_password=models.CharField(max_length=100)
    image=models.ImageField(upload_to='customer/',default='')


    class Meta:
        db_table='customer'

       




    
