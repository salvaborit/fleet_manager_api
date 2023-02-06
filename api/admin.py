from django.contrib import admin

from .models import Vehicle
from .models import VehicleModel
from .models import Documentation


admin.site.register(Vehicle)
admin.site.register(VehicleModel)
admin.site.register(Documentation)
