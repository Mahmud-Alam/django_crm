from django.shortcuts import redirect, render
from django.forms import inlineformset_factory

from .models import *
from .form import *
from .filters import *

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

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_order = orders.count()
    
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer':customer, 'orders':orders, 'total_order':total_order, 'myFilter':myFilter}
    return render(request, 'accounts/customer.html', context)

def createOrder(request, cpk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'), extra=6)       #extra=6 show 6 form sets
    customer = Customer.objects.get(id=cpk)
    customerInitial = {'customer':customer}
    #form = OrderForm(initial=customerInitial)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)                        #queryset=Order.objects.none() doesn't show previous orders.
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('home')

    context = {'formset':formset}
    return render(request, 'accounts/order-form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'accounts/order-form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('home')

    context = {'item':order}
    return render(request, 'accounts/delete.html', context)
