from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('test', views.TestViewSet)

urlpatterns = [
    path('status/', views.APIStatus.as_view(), name='api_status'),
] + router.urls
