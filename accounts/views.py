from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    total_customers = customers.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders,'customers':customers, 'total_orders':total_orders, 'total_customers':total_customers, 'delivered':delivered, 'pending':pending}
    
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'accounts/products.html', context)

def customer(request):
    customers = Customer.objects.all()
    context = {'customers':customers}
    return render(request, 'accounts/customer.html', context)