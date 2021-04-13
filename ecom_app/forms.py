from .models import *
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

class OwnerRegisterForm(forms.ModelForm):
    class Meta:
        model = OwnerRegister
        fields = '__all__'
        exclude = ('user','is_owner')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = CustomerRegister
        fields = '__all__'
        exclude = ('user','is_customer')

class HomeForm(forms.ModelForm):
    name = forms.CharField()
    class Meta:
        model = product_info
        fields = '__all__'
        exclude =('product_status','user')