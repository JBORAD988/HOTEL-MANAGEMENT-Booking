from django.contrib import admin

from .models import Contact,Hotel,Rooms,Reservation
# Register your models here.


admin.site.register(Contact)
admin.site.register(Hotel)
admin.site.register(Rooms)
admin.site.register(Reservation)