from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Bus(models.Model):
    bus_name = models.CharField(max_length=100)
    number = models.CharField(max_length=100, unique=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    no_of_seats = models.PositiveIntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.bus_name}-{self.number}"


class Seat(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.seat_number


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.bus.bus_name}-{self.seat.seat_number}"
