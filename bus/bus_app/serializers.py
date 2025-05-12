from rest_framework import serializers
from .models import Bus, Seat
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = "__all__"


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ["id", "seat_number", "is_booked"]
