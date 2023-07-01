from django.db import models
from doc.models import Doc
from phonenumber_field.modelfields import PhoneNumberField

class Patient(models.Model):
    name = models.TextField()
    weight = models.IntegerField()
    heigth = models.IntegerField()
    gender = models.TextField()
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField()
    uuid = models.UUIDField(primary_key=True, unique=True, editable=False)
    address = models.TextField()
    past_allergies = models.TextField(blank=True)
    past_operations = models.TextField(blank=True)
    past_treatment = models.TextField(blank=True)


class Prescription(models.Model):
    doc_id = models.OneToOneField(Doc, on_delete=models.CASCADE)
    patient_id = models.OneToOneField(Patient, on_delete=models.CASCADE)
    medicine = models.TextField()
    symptoms = models.TextField()
