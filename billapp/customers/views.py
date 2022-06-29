from distutils.command.upload import upload
from django.shortcuts import redirect, render
from apps.models import App
from .models import Customer
from .forms import CustomerCreateForm
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.


def create_customer(request, slug):
    app = App.objects.get(slug=slug)
    if request.method == 'POST':
        form = CustomerCreateForm(request.POST)
        if request.user == app.author:
            if form.is_valid():
                Customer.objects.create(
                    name = request.POST.get('name'),
                    email = request.POST.get('email'),
                    contact_number = request.POST.get('contact_number'),
                    address = request.POST.get('address'),
                    utility=request.POST.get('utility'),
                    app = app
                )
                messages.success(request, f"customer account has been added")
                return redirect('dashboard', slug=slug)
        else :
            messages.warning(request, f"you are not authorized to do this action")
            return redirect('home')
    else :
        form = CustomerCreateForm()
    return render(request, 'customers/addcustomer.html', {'form' :form})


def delete_customer(request, slug, id):
    customer = Customer.objects.get(id=id)
    if request.user == customer.app.author:
        customer.delete()
        messages.success(request, f"customer account has been succesfully deleted")
        return redirect('customerlist', slug=slug)
    else :
        messages.warning(request, f"you are not authorized to do this action")
        return redirect('home')


def edit_customer(request, slug, id):
    app = App.objects.get(slug=slug)
    customer = Customer.objects.get(id=id)
    if request.user == customer.app.author:
        if request.method == 'POST':
            form = CustomerCreateForm(request.POST, instance=customer)
            if form.is_valid():
                customer.name = request.POST.get('name')
                customer.email = request.POST.get('email')
                customer.contact_number = request.POST.get('contact_number')
                customer.address = request.POST.get('address')
                customer.utility=request.POST.get('utility')
                customer.save()
                messages.success(request, f"customer account has been updated")
                return redirect('dashboard', slug=slug)
        else :
            form = CustomerCreateForm(instance=customer)
            return render(request, 'customers/editcustomer.html', {'form' : form})
    else :
        messages.warning(request, f"you are not authorized to do this action")
        return redirect('home')


def dashboard(request, slug):
    app = App.objects.get(slug=slug)
    count = app.customer_set.count()
    columns=[field.name for field in Customer._meta.get_fields()]
    details = Customer.objects.all().filter(app=app)[:5]
    return render(request, 'customers/dashboard.html', {'count' : count, 'columns':columns, 'details':details, 'slug' : slug})

def customerlist(request, slug):
    app = App.objects.get(slug=slug)
    columns=[field.name for field in Customer._meta.get_fields()]
    details = Customer.objects.all().filter(app=app)
    return render(request, 'customers/customerlist.html', {'columns':columns, 'details':details})


def estimates(request, slug):
    return HttpResponse('<h1>Estimates</h1>')

def settings(request, slug):
    return HttpResponse('<h1>Settings</h1>')

def bulkupload(request, slug):
    return HttpResponse('<h1>Bulk Upload</h1>')

def manage_group(request, slug):
    return HttpResponse('<h1>Manage Group</h1>')

def pending_approvals(request, slug):
    return HttpResponse('<h1>Pending Approvals</h1>')

def messaging(request, slug):
    return HttpResponse('<h1>Messaging</h1>')

def collect_payments(request, slug):
    return HttpResponse('<h1>Collect Payments</h1>')

def transactions(request, slug):
    return HttpResponse('<h1>Transactions</h1>')

def plans(request, slug):
    return HttpResponse('<h1>Plans</h1>')

def requests(request, slug):
    return HttpResponse('<h1>Requests</h1>')

def get_support(request, slug):
    return HttpResponse('<h1>Get Support</h1>')