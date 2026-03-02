from django.db import models

class Product(models.Model):  # Make sure 'Product' is spelled correctly here
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.quantity} in stock)"

from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # ADD THIS LINE (The "Flawed" Code):
    # Change TextField to CharField
description = models.CharField(max_length=255, blank=True, null=True) 

    def __str__(self):
        return self.name    