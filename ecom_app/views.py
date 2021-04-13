from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
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
            form_b.is_owner = True
            form_b.save()
            return HttpResponseRedirect(reverse('ecom_app:Owner_login'))
        else:
            print(form.errors,form_a.errors)
    else:
        form = UserForm()
        form_a = OwnerRegisterForm()
        return render(request,'top/Owner_register.html',{'form':form,'form_a':form_a})


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
            form_b.is_customer = True
            form_b.save()
            return HttpResponseRedirect(reverse('ecom_app:Owner_login'))
        else:
            print(form.errors,form_a.errors)
    else:
        form = UserForm()
        form_a = CustomerRegisterForm()
    return render(request,'top/Customer_register.html',{'form':form,'form_a':form_a})


 ####################################################################################
def Owner_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                try:
                    data = CustomerRegister.objects.get(user_id=user)
                    
                    if data.is_customer == True:
                        login(request, user)
                        print("demo_user")
                        return HttpResponseRedirect(reverse('ecom_app:index_c'))
                    else:
                        return HttpResponse("demo1")
                except:
                    data2 = OwnerRegister.objects.get(user_id=user)
                    if data2.is_owner == True:
                        login(request, user)
                        return HttpResponseRedirect(reverse('ecom_app:index'))
                    else:
                        return HttpResponse("demo2")
            else:
                print('user is not active')
                return HttpResponse("demo3")
        else:
            messages.info(request, 'Username or password is wrong!')
            return HttpResponseRedirect(reverse('ecom_app:Owner_login'))
    else:
        return render(request, 'top/login.html')

def owner_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('ecom_app:home'))


 ####################################################################################

def home(request):
    if request.method == 'POST':
        form = HomeForm(request.POST,request.FILES)
        if form.is_valid():
            form_a = form.save(commit=False)
            form_a.product_status = True
            form_a.save()
            return HttpResponse('welcome is page')
        else:
            print(form.errors)

    else:
        form = HomeForm()
    return render(request,'top/home.html',{'form':form})

def product(request):
    if request.method == 'POST':
        form = HomeForm(request.POST,request.FILES)
        if form.is_valid():
            form_a = form.save(commit=False)
            form_a.product_status = True 
            form_a.save()
            return HttpResponseRedirect(reverse('ecom_app:index'))
        else:
           print(form.errors)
    else:
        form = HomeForm()
    return render(request,'top/main.html',{'form':form})

def customer_home(request):
    form = HomeForm()
    return render(request,'top/customer_home.html',{'form':form})
            

#######################################################################################

def index(request):
    data = product_info.objects.all()
    return render(request,'top/index.html',{'data':data})

@login_required
def index_c(request):
    big = product_info.objects.all()
    return render(request,'top/index_c.html',{'big':big})


########################################################################################

def update(request,id):
    instance = product_info.objects.get(id=id)
    form = HomeForm(request.POST or None ,request.FILES or None , instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('ecom_app:index'))
    else:
        print(form.errors)
    return render(request,'top/update.html',{'form':form})

def delete(request,id):
    data = product_info.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('ecom_app:index'))

def details(request,id):
    data = product_info.objects.get(id=id)
    return render(request,'top/details.html',{'data':data})

#########################################################################################
#(add_to_cart)

def add_to_cart(request, id):
    item = get_object_or_404(product_info, id=id)
    order_item, created = OrderItem.objects.get_or_create(Product=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs .exists():
        order = order_qs[0]
        if order.item.filter(Product_id=item.pk).exists():
            order_item.quntity += 1
            order_item.save()
            messages.info(request, "Item Quantity was updated.")
            return redirect('ecom_app:index_c')
        else:
            messages.info(request, "Item was added to a cart.")
            order.item.add(order_item)
            return redirect('ecom_app:index_c')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.item.add(order_item)
        messages.info(request, "Item was added to a cart.")
    return redirect('ecom_app:index_c')


