from django.contrib import admin
from .models import UserInfo, ParkingSpace, Reservation, VehicleType, Payment, ReservationModel
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(ParkingSpace)
admin.site.register(VehicleType)
admin.site.register(Payment)
admin.site.register(ReservationModel)
