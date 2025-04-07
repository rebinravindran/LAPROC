from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from app.models import User
from customers.models import Customer
from products.models import Product
from seller.models import Seller,Approve_Seller
from seller.views import *
from products.views import *
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView




class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'  # Your custom template for the password reset form
    email_template_name = 'registration/password_reset_email.html'  # Your custom template for the password reset email
    success_url = '/accounts/password_reset/done/'  # URL to redirect after the password reset email is sent

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'  # Your custom template for the password reset confirmation form
    success_url = '/accounts/password_reset/complete/'  # URL to redirect after the password is reset successfully