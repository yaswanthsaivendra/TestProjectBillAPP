from ast import arg
from django.db import models
from apps.models import App

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    utility = models.CharField(max_length=50)
    address = models.TextField()
    app = models.ForeignKey(App, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"customer name: {self.name}"


    