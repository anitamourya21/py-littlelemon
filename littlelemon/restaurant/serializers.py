from django.db import models
from rest_framework import serializers
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('title', 'price')


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'