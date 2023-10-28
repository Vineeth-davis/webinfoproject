
from django.db import models
from django.contrib.auth.models import Group, User
from django.contrib.auth.models import AbstractUser

import re
from django.core.exceptions import ValidationError

class Platform(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=100)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

def validate_ip_address(value):
    ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    if not re.match(ip_pattern, value):
        raise ValidationError("Invalid IP address format")

    ip_value = value.split('.')
    for val in ip_value:
        if not 0 <= int(val) <= 255:
            raise ValidationError("IP address provided is out of range (0-255)")

class Device(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=15, validators=[validate_ip_address])
    username = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            device = Device.objects.get(pk=self.pk)
            self.platform = device.platform
            self.product = device.product
        super(Device, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
