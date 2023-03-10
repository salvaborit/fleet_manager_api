from rest_framework.routers import SimpleRouter

from .views import VehicleViewSet
from .views import DriverViewSet
from .views import VehicleDocumentationViewSet
from .views import DriverDocumentationViewSet


router = SimpleRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'vehicle-docs', VehicleDocumentationViewSet)
router.register(r'driver-docs', DriverDocumentationViewSet)

urlpatterns = router.urls
