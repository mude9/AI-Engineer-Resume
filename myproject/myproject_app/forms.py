# forms.py
from django import forms
from .models import Order
# authentication/forms.py



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'card_number', 'expiry_date', 'cvv']
