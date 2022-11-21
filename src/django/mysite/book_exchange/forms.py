from django import forms

from .models import Book

class SellForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['available', 'seller']