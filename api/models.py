# models.py

from django.db import models

class Client(models.Model):
    document = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    token = models.CharField(max_length=255, blank=True, null=True)

class Bill(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dacompany_name = models.CharField(max_length=255)
    nit = models.CharField(max_length=255)
    code = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class BillProduct(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)