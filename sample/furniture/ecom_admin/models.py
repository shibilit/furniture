from django.db import models

# Create your models here.
class Appadmin(models.Model):
    A_username=models.CharField(max_length=100)
    A_pssword=models.CharField(max_length=50)

    class Meta:
        db_table ='app_admin'

class Category(models.Model):
    category_name=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    image=models.ImageField(upload_to='category/')

    class Meta:
        db_table = 'category'
