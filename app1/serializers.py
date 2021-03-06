#from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model= Contact
        fields= [
            'first_name',
            'last_name',
            'phone_no',
            'id',
        ]