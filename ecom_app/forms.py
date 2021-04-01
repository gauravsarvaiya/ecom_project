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
        exclude = ('user',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = CustomerRegister
        fields = '__all__'
        exclude = ('user',)