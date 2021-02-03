from django import forms
from .models import Order
from crispy_forms.helper import FormHelper

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["order_by","mobile","email","pin_code","shiping_address","payment_method"]

        widgets = {
            'order_by': forms.TextInput(attrs = {'class':'form-contol','placeholder': '1234 Main St'}),
            'mobile': forms.TextInput(attrs = {'class':'form-contol','placeholder': 'Phone No.'}),
            'email': forms.EmailInput(attrs = {'class':'form-contol','placeholder': 'example@xyz.com'}),
            'pin_code': forms.TextInput(attrs = {'class':'form-contol','placeholder': 'zip code.......'}),
            'shiping_address': forms.Textarea(attrs = {'class':'form-contol','placeholder': 'Ente delivery address.......'}),            
        }