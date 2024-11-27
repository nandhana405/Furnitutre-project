from django.db import models

# Create your models here.

class ContactDb(models.Model):
    First_name=models.CharField(max_length=100,null=True,blank=True)
    Last_name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Message=models.TextField(max_length=400,null=True,blank=True)


class SignupDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Mail=models.EmailField(max_length=100,null=True,blank=True)
    Mobile=models.IntegerField(max_length=100,null=True,blank=True)
    Pass1=models.CharField(max_length=100,null=True,blank=True)
    Pass2=models.CharField(max_length=100,null=True,blank=True)

class CartDb(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    productname=models.CharField(max_length=100,null=True,blank=True)
    quantity=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField(max_length=100,null=True,blank=True)
    totalprice=models.IntegerField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to="cart",null=True,blank=True)

class orderDb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    place=models.CharField(max_length=100,null=True,blank=True)
    mail=models.EmailField(max_length=100,null=True,blank=True)
    address=models.TextField(max_length=100,null=True,blank=True)
    mobile=models.CharField(max_length=100,null=True,blank=True)
    message=models.TextField(max_length=100,null=True,blank=True)
    total_price=models.IntegerField(max_length=100,null=True,blank=True)
