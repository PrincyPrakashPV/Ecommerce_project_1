from operator import mod
from django.db import models
from shop.models import *

# Create your models here.
class cartlist(models.Model):
    cart_id=models.CharField(max_length=300,unique=True)
    date_add=models.DateTimeField(auto_now_add=True)

    def __str(self):
        return self.cart_id

class items(models.Model):
    prodt=models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    qty=models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.prodt

    def total(self):
        return self.qty * self.prodt.price

 