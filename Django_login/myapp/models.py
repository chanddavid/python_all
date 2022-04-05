
from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

CATEGORY_CHOICES={
    ('Electronic','Electronic'),
    ('Clothes','Clothes'),
    ('Kitchen','Kitchen'),
    ('shoes','shoes'),
}

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    category=models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description=models.CharField(max_length=100,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name


STATUS_CHOICES={
    ('Pending','Pending'),
    ('Out of delivery','Out of delivery'),
    ('Delivered','Delivered'),
    ('Packed','Packed'),  
}

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    date_ordered=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(choices=STATUS_CHOICES,null=True,max_length=100)
    review=models.CharField(max_length=100,null=True)