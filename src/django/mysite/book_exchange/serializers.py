from django.db.models import fields
from rest_framework import serializers
from .models import School

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('school_name', 'city', 'state')