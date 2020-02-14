from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Account(models.Model):
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    user_check = models.BooleanField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
