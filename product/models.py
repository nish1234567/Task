from distutils.command.upload import upload
from operator import mod
from pyexpat import model
from tkinter import CASCADE
from turtle import color
from unicodedata import category
from django.db import models
from django.utils.text import slugify
from matplotlib import image
from matplotlib.pyplot import cla
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(max_length=500, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name

class QuantityVariant(models.Model):
    Variant_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.Variant_name

class ColorVariant(models.Model):
    color_name = models.CharField(max_length=200, blank=True)
    color_code = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.color_name

class SizeVariant(models.Model):
    size_name = models.CharField(max_length=35)

    def __str__(self):
        return self.size_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to = 'static/products')
    price = models.CharField(max_length=150, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    stock = models.IntegerField(default=100)
    quantity_type = models.ForeignKey(QuantityVariant, on_delete=models.PROTECT, null=True)
    color_type = models.ForeignKey(ColorVariant, on_delete=models.PROTECT, null=True)
    size_type = models.ForeignKey(SizeVariant, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.product_name

class Meta:
    pass