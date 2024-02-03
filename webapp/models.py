from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=False)
    gender = models.CharField(max_length=50)
    contact = models.IntegerField(blank=False)
    address = models.CharField(max_length=50)
    def __str__(self):
        return self.name
 
class ParkingSpace(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    
    reservation_date = models.DateField()
    reservation_time_start = models.TimeField()
    reservation_time_end = models.TimeField()
    
class VehicleType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Payment(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reservation.user.username} - {self.amount} USD"

from django.db import models

class ReservationModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField()
    arrival_time = models.TimeField()
    vehicle_type = models.CharField(max_length=255)

    def __str__(self):
        return self.name
