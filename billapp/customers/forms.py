from dataclasses import fields
from django import forms
from .models import Customer


class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'contact_number', 'utility', 'address']
