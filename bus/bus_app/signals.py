from django.db.models.signals import post_save
from .models import Bus, Seat
from django.dispatch import receiver


@receiver(post_save, sender=Bus)
def create_seats_for_bus(sender, instance, created, **kwargs):
    if created:
        for i in range(1, instance.no_of_seats + 1):
            Seat.objects.create(bus=instance, seat_number=f"S{i}")
