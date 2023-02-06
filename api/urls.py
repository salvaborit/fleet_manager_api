from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import VehicleViewSet
from .views import VehicleDocumentationViewSet
from .views import DriverDocumentationViewSet


router = SimpleRouter()
router.register('vehicles', VehicleViewSet)
router.register('drivers', VehicleViewSet)
router.register('vehicle-docs', VehicleDocumentationViewSet)
router.register('driver-docs', DriverDocumentationViewSet)

urlpatterns = router.urls
