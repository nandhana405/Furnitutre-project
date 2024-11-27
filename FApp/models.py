from django.db import models

# Create your models here.

class Category_Db(models.Model):
    category_name=models.CharField(max_length=100, null=True,blank=True)
    description=models.TextField(max_length=100, null=True,blank=True)
    category_image=models.ImageField(upload_to="Category",null=True,blank=True)


class Product_Db(models.Model):
    category=models.CharField(max_length=100, null=True,blank=True)
    product_name=models.CharField(max_length=100, null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    mrp=models.IntegerField(null=True,blank=True)
    description=models.CharField(max_length=100, null=True,blank=True)
    country=models.CharField(max_length=100, null=True,blank=True)
    manufactured=models.CharField(max_length=100, null=True,blank=True)
    image1=models.ImageField(upload_to="Product",null=True,blank=True)
    image2=models.ImageField(upload_to="Product",null=True,blank=True)
    image3=models.ImageField(upload_to="Product",null=True,blank=True)

