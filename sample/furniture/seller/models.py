
from django.db import models
from ecom_admin.models import Category



# Create your models here.
class Product(models.Model):
    pro_name=models.CharField(max_length=100)
    pro_number=models.CharField(max_length=300)
    pro_category=models.ForeignKey(Category,on_delete=models.CASCADE,default='')
    pro_description=models.CharField(max_length=400)
    pro_price=models.BigIntegerField()
    pro_quantity=models.BigIntegerField()
    
    pro_image=models.ImageField(upload_to='seller/')

    class Meta:
        db_table = 'product'
