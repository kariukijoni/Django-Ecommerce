from django.contrib import admin
from .models import *

# # Register your models here.
model_list=[Customer,Product,Order,OrderItem,ShippingAddress]

admin.site.register(model_list)