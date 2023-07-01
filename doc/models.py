from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Doc(models.Model):
    name = models.TextField()
    weight = models.IntegerField()
    heigth = models.IntegerField()
    gender = models.TextField()
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField()
    uuid = models.UUIDField(primary_key=True, unique=True, editable=False)
    