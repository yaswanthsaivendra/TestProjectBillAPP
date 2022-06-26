from django.urls import path
from .views import create_customer, dashboard, customerlist, delete_customer, edit_customer


urlpatterns = [
    path('addcust/', create_customer, name='create-customer'),
    path('', dashboard, name='dashboard'),
    path('customerlist/', customerlist, name='customerlist'),
    path('<int:id>/deletecustomer/', delete_customer, name='deletecustomer'),
    path('<int:id>/editcustomer/', edit_customer, name='edit-customer'),

]