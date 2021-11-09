from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/',views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.userPage, name='user'),

    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>', views.customer, name='customer'),

    path('account/', views.accountSettings, name='account'),
    
    path('create-order/<str:cpk>', views.createOrder, name='create-order'),
    path('update-order/<str:pk>', views.updateOrder, name='update-order'),
    path('delete-order/<str:pk>', views.deleteOrder, name='delete-order'),


    # for email password reset with django template
    path('reset-password/',auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset-password-sent/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password-complete/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

"""
from the documentation: https://docs.djangoproject.com/en/3.2/topics/auth/default/#all-authentication-views
1 - Submit email form                           PasswordResetView.as_view()
2 - Email sent success message                  PasswordResetDoneView.as_view()
3 - Link to password Reset from in email        PasswordResetConfirmView.as_view()
4 - Password successfully changed message       PasswordResetCompleteView.as_view()
"""