from django.db import models
from doc.models import Doc
from phonenumber_field.modelfields import PhoneNumberField
import uuid

class Patient(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    gender = models.TextField()
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField()
    uuid = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    address = models.TextField()
    past_allergies = models.TextField(blank=True)
    past_operations = models.TextField(blank=True)
    past_treatment = models.TextField(blank=True)
    short_uuid = models.CharField(max_length=10, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.short_uuid:
            self.short_uuid = str(self.uuid)[:10]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.short_uuid}"

class Report(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    symtoms = models.TextField()
    medicine = models.TextField()


    def __str__(self):
        return f"{self.uuid}"