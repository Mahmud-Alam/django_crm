from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>', views.customer, name='customer'),
    
    path('create-order', views.createOrder, name='create-order'),
    path('update-order/<str:pk>', views.updateOrder, name='update-order'),
    path('delete-order/<str:pk>', views.deleteOrder, name='delete-order'),
]
