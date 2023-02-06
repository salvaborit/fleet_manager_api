from django.contrib import admin

from .models import Vehicle
from .models import Driver
from .models import VehicleModel
from .models import VehicleDocumentation
from .models import DriverDocumentation


admin.site.register(Vehicle)
admin.site.register(Driver)
admin.site.register(VehicleModel)
admin.site.register(VehicleDocumentation)
admin.site.register(DriverDocumentation)
