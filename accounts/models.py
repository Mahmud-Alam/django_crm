from django.db import models
from django.db.models.base import Model

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    CATEGORY = (
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),
    )

    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    category = models.CharField(max_length=200,choices=CATEGORY, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )

    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, choices=STATUS, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.name
