from django.db import models
from django.utils.translation import gettext_lazy as _


class VehicleModel(models.Model):
    make = models.CharField(max_length=63)
    model = models.CharField(max_length=63)

    def __str__(self):
        return f'{self.make} {self.model}'


class Documentation(models.Model):

    class StatusChoices(models.TextChoices):
        """ Choices for the type of vehicle usage """
        VALID = 'VAL', _('Valido')
        EXPIRED = 'EXP', _('Expirado')

    title = models.CharField(max_length=256)
    valud_thru = models.DateTimeField()
    renovation_alert = models.DateTimeField(
        auto_now=False,
        auto_now_add=False)
    status = models.CharField(
        max_length=3,
        choices=StatusChoices.choices,
        default=StatusChoices.VALID)

    def __str__(self):
        return f'{self.status}, {self.title}, expires in: {self.valid_thru}'


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

    license_plate = models.CharField(max_length=15)
    model = models.ForeignKey(VehicleModel, on_delete=models.PROTECT)
    status = models.CharField(
        max_length=2,
        choices=StatusChoices.choices,
        default=StatusChoices.ACTIVE)
    usage_type = models.CharField(
        max_length=2,
        choices=UsageTypeChoices.choices,
        default=UsageTypeChoices.KMS)
    usage = models.PositiveIntegerField()
    documentation = models.ForeignKey(
        Documentation,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True)

    def __str__(self):
        return f'{self.model} with license plate {self.license_plate}'
