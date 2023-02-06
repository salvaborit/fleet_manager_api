from django.urls import path

from .views import APIStatus


urlpatterns = [
    path('status/', APIStatus.as_view())
]
