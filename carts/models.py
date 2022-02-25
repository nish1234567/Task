from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from matplotlib.pyplot import cla
from product.models import Product
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from product import views
from accounts import views
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_field = models.FloatField(default=0)

    def __str__(self):
        return str(self.user.username) + "" + str(self.product_name)

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    total_items = models.IntegerField(blank=True, default=0)
    quantity = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return str(self.user.username) + "" + str(self.product_name)

@receiver(pre_save, sender=CartItems)
def Correct_price(sender,**kwargs):
    cart_items = kwargs['instance']
    price_of_product = Product.objects.get(id = cart_items.product.id)
    cart_items.price = cart_items.quantity*float(price_of_product.price)
    total_cart_items = CartItems.objects.filter(user = cart_items.user)
    #cart = Cart.objects.all(id=cart_items.cart.id)
    #cart.total_price = cart_items.price
    #cart.save()