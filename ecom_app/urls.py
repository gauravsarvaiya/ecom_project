from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'ecom_app'

urlpatterns = [
  path('Owner_register/',views.Owner_register,name="Owner_register"),
  path('Customer_register/',views.Customer_register,name="Customer_register"),

]