from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def Owner_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        form_a = OwnerRegisterForm(request.POST)
        if form.is_valid() and form_a.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            form_b = form_a.save(commit=False)
            form_b.user = user
            form_b.save()
            return HttpResponseRedirect(reverse('ecom_app:login'))
        else:
            print(form.errors,form_a.errors)
    else:
        form = UserForm()
        form_a = OwnerRegisterForm()
    return render(request,'top/Owner_register.html',{'form':form,'form_a':form_a})

def Owner_login(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username ,password = password)
        if user:
            if user.is_active:
                try:
                    is_owner = OwnerRegister.objects.get(user_id=user)
                    if .is_owner == True:
                        return HttpResponseRedirect(reverse('ecom_app:home'))
                except:
                    is_Customer = CustomerRegister.objcets.get(user_id=user)
                    if is_Customer == is_Customer:
                        return HttpResponseRedirect(reverse('ecom_app:owner_login'))

                login(request, user)
                return HttpResponseRedirect(reverse('demo_app:home'))
            else:
                print('user not active')
        else:
            messages.info(request,'Username Or Password are worng!!')
            return HttpResponseRedirect(reverse('demo_app:user_login'))
    else:

        return render(request,'top/user_login.html')


 


 #######################################################################################
def Customer_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        form_a = CustomerRegisterForm(request.POST)
        if form.is_valid() and form_a.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            form_b = form_a.save(commit=False)
            form_b.user = user
            form_b.save()
            return HttpResponseRedirect(reverse('ecom_app:login'))
        else:
            print(form.errors,form_a.errors)
    else:
        form = UserForm()
        form_a = CustomerRegisterForm()
    return render(request,'top/Customer_register.html',{'form':form,'form_a':form_a})
