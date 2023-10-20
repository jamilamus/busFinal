from django.contrib import admin
from .models import BusRoute, Driver, Bus, Stop

admin.site.register(BusRoute)
admin.site.register(Driver)
admin.site.register(Bus)
admin.site.register(Stop)
