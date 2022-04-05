from django.contrib import admin
from .models import Customer,Order,Product
# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','name','email','phone','date_created']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','name','price','category','description','date_created']

@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display=['id','customer','product','date_ordered','status']