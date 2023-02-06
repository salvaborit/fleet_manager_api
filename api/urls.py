from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import VehicleViewSet
from .views import VehicleModelViewSet
from .views import DocumentationViewSet


router = SimpleRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'models', VehicleModelViewSet)
router.register(r'documentations', DocumentationViewSet)

urlpatterns = router.urls
