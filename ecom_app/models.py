from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator




class OwnerRegister(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)

    

    def __str__(self):
        return self.user.first_name

class CustomerRegister(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_customer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

    
class product_info(models.Model):
    user = models.ForeignKey(OwnerRegister, on_delete=models.CASCADE,null =True,blank=True)
    product_name = models.CharField(max_length=100)
    product_prize = models.IntegerField()
    product_material = models.CharField(max_length=50)
    product_brand = models.CharField(max_length = 40)
    product_status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.product_name


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    Product = models.ForeignKey(product_info, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quntity = models.IntegerField(default=1)

    def __str__(self):
        return self.Product.product_name



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name





    
    
    
    
