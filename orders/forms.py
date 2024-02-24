from django import forms
from django.utils.translation import gettext as _

from .models import Order, OrderItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'order_notes']
        widgets = {
            'order_notes': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': _('If You Have Any Words Please Enter Here!'),
            }),
            'address': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': _('Enter Your Address Here!'),

            }),
        }


