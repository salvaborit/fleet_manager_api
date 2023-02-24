from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


class Vehicle(models.Model):
    """ Vehicle model """

    class UsageTypeChoices(models.TextChoices):
        """ Choices for the type of vehicle usage """
        KMS = 'KM', _('Kilometros')
        HRS = 'HR', _('Horas')

    class StatusChoices(models.TextChoices):
        """ Choices for the vehicle status """
        ACTIVE = 'AC', _('Activo')
        MAINTENANCE = 'MA', _('Mantenimiento')
        REPAIR = 'TA', _('Taller')
        INACTIVE = 'IN', _('Inactivo')

    license_plate = models.CharField(
        max_length=15, unique=True)
    model = models.CharField(
        max_length=63)
    status = models.CharField(
        max_length=2,
        choices=StatusChoices.choices,
        default=StatusChoices.ACTIVE)
    usage_type = models.CharField(
        max_length=2,
        choices=UsageTypeChoices.choices,
        default=UsageTypeChoices.KMS)
    usage = models.PositiveIntegerField()
    notes = models.TextField(
        blank=True)

    def __str__(self):
        return f'{self.license_plate} {self.model}'


class Driver(models.Model):
    """ Driver Model """
    class IDTypeChoices(models.TextChoices):
        """ Choices for the driver id type """
        CI = 'CI', _('Cedula')
        PASSPORT = 'PA', _('Pasaporte')

    def validate_alphanumeric(value):
        if not re.match('^[0-9a-zA-Z]+$', value):
            raise ValidationError(
                'ID number should only contain alphanumeric characters.')

    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=127)
    phone = models.CharField(max_length=31)
    birthdate = models.DateField(
        auto_now=False,
        auto_now_add=False)
    id_type = models.CharField(
        max_length=2,
        choices=IDTypeChoices.choices,
        default=IDTypeChoices.CI)
    id_number = models.CharField(
        max_length=31,
        validators=[validate_alphanumeric])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class VehicleDocumentation(models.Model):
    """ Vehicle Documentation model """

    class RenovationAlert(models.IntegerChoices):
        # in days
        FIFTEEN_DAYS = 15
        THIRTY_DAYS = 30
        FORTY_FIVE_DAYS = 45
        SIXTY_DAYS = 60

    title = models.CharField(max_length=255)
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        null=True)
    expiry = models.DateField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True)
    renovation_alert = models.IntegerField(
        choices=RenovationAlert.choices,
        null=True,
        blank=True)

    def __str__(self):
        return f'{self.title} de {self.vehicle}, expira en {self.expiry}'


class DriverDocumentation(models.Model):
    """ Driver Documentation model """

    class RenovationAlert(models.IntegerChoices):
        # in days
        FIFTEEN_DAYS = 15
        THIRTY_DAYS = 30
        FORTY_FIVE_DAYS = 45
        SIXTY_DAYS = 60

    title = models.CharField(max_length=256)
    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        null=True)
    expiry = models.DateField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True)
    renovation_alert = models.IntegerField(
        choices=RenovationAlert.choices,
        null=True,
        blank=True)

    def __str__(self):
        return f'{self.title} de {self.driver}, expira en {self.expiry}'


class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    usage_at_entry = models.PositiveIntegerField()
    next_maintenance_usage = models.PositiveIntegerField()
    entry_date = models.DateField(auto_now=False,
                                  auto_now_add=False)
