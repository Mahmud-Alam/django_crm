from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>', views.customer, name='customer'),
    
    path('create-order/<str:cpk>', views.createOrder, name='create-order'),
    path('update-order/<str:pk>', views.updateOrder, name='update-order'),
    path('delete-order/<str:pk>', views.deleteOrder, name='delete-order'),
]
