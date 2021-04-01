from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Product(models.Model):
    product_name = models.CharField(max)



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

    


    
    
    
    
