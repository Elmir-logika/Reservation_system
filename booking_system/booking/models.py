from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.room.name} from {self.start_date} to {self.end_date}"
