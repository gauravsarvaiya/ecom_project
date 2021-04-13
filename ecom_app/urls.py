from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'ecom_app'

urlpatterns = [
  path('Owner_register/',views.Owner_register,name="Owner_register"),
  path('Customer_register/',views.Customer_register,name="Customer_register"),
  path('Owner_login/',views.Owner_login,name = "Owner_login"),
  path('',views.home,name ="home"),
  path('main/',views.product,name="Main"),
  path('update/<int:id>',views.update,name="update"),
  path('delete/<int:id>',views.delete,name ="delete"),
  path('details/<int:id>',views.details,name = "details"),
  path('customer/',views.customer_home,name="customer_home"),
  path('index/',views.index,name ="index"),
  path('index_c/',views.index_c,name="index_c"),
  path('logout/',views.owner_logout,name = "logout"),
  path('add_to_cart/<int:id>',views.add_to_cart, name='add_to_cart')
]