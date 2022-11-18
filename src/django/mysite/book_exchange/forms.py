from django import forms

from .models import BookForSale

class SellForm(forms.ModelForm):
    class Meta:
        model = BookForSale
        exclude = ['ISBN', 'seller', 'available']
