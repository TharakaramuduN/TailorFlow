from django.contrib import admin
from .models import *


# admin.site.register(Measurements)
# admin.site.register(Products)
# admin.site.register(Transactions)


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'Name',
                    'Village', 'Phone', 'Gmail', 'profilephoto']
    search_fields = ['Name', 'Village', 'Phone', 'Gmail']


@admin.register(Measurements)
class MeasurementsAdmin(admin.ModelAdmin):
    list_display = ["customer", "Neck", "Chest", "Waist", "Hips", "Thigh", "Knee", "Calf",
                    "Sleeve", "Back", "Waistband", "Outseam", "Inseam", "Ankle"]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product_name', 'garment_drop_off',
                    'requested_pick_up_date', 'garment_pick_up', 'price', 'design', 'clothimage']


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ['customer', 'amount',
                    'payment_date', 'total_amount', 'advance_amount']
