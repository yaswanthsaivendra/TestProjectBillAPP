from django.urls import path
from .views import (
    create_customer,
    dashboard, 
    customerlist, 
    delete_customer, 
    edit_customer, 
    estimates, 
    settings, 
    bulkupload,
    manage_group,
    pending_approvals,
    messaging,
    collect_payments,
    transactions,
    plans,
    requests,
    get_support
)


urlpatterns = [
    path('addcust/', create_customer, name='create-customer'),
    path('dashboard/', dashboard, name='dashboard'),
    path('customerlist/', customerlist, name='customerlist'),
    path('<int:id>/deletecustomer/', delete_customer, name='deletecustomer'),
    path('<int:id>/editcustomer/', edit_customer, name='edit-customer'),
    path('estimates/', estimates, name='estimates'),
    path('settings/', settings, name='settings'),
    path('bulkupload/', bulkupload, name='bulkupload'),
    path('manage_group/', manage_group, name='manage_group'),
    path('pending_approvals/', pending_approvals, name='pending_approvals'),
    path('messaging/', messaging, name='messaging'),
    path('collect_payments/', collect_payments, name='collect_payments'),
    path('transactions/', transactions, name='transactions'),
    path('plans/', plans, name='plans'),
    path('requests/', requests, name='requests'),
    path('get_support/', get_support, name='get_support'),
]