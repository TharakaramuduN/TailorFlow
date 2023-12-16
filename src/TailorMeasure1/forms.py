from django import forms
from .models import Customers, Measurements, Products, Transactions


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['Name', 'Village', 'Phone', 'Gmail']


class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurements
        fields = ["Neck", "Chest", "Waist", "Hips", "Thigh", "Knee", "Calf",
                  "Sleeve", "Back", "Waistband", "Outseam", "Inseam", "Ankle"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'garment_drop_off',
                  'requested_pick_up_date', 'garment_pick_up']


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['amount', 'payment_date', 'total_amount', 'advance_amount']
