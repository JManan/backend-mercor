from django.db import models
from doc.models import Doc
from phonenumber_field.modelfields import PhoneNumberField
import uuid

class Patient(models.Model):
    name = models.TextField()
    weight = models.IntegerField()
    heigth = models.IntegerField()
    gender = models.TextField()
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField()
    uuid = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    address = models.TextField()
    past_allergies = models.TextField(blank=True)
    past_operations = models.TextField(blank=True)
    past_treatment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} {self.uuid}"

class Report(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    symtoms = models.TextField()
    medicine = models.TextField()

    def __str__(self):
        return f"{self.uuid}"