from django.db.models import fields
from rest_framework import serializers
from .models import School, User, Book, PinnedBook, Transaction

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['school_name', 'city', 'state']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'city', 'state', 'school_name', 'year', 'major',]

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['ISBN', 'title', 'edition', 'author_first_name', 'author_last_name', 'subject', 'topic']

class PinnedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = PinnedBook
        fields = ['user', 'book_listing']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['buyer', 'book_listing', 'time_sold']