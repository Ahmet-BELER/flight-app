from django.contrib import admin
from .models import (
    Country,
    City,
    UserType,
    Airport,
    Company,
    Flight,
    Reservation,
)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(UserType)
admin.site.register(Airport)
admin.site.register(Company)
admin.site.register(Flight)
admin.site.register(Reservation)

# Register your models here.
