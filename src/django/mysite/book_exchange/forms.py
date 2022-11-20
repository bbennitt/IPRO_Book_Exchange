from django import forms

from .models import BookForSale, Book

class SellForm(forms.ModelForm):
    class Meta:
        model = BookForSale
        exclude = ['available']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"