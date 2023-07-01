from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid

class Doc(models.Model):
    name = models.TextField()
    weight = models.IntegerField()
    heigth = models.IntegerField()
    gender = models.TextField()
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField()
    uuid = models.UUIDField(primary_key=True, unique=True,default = uuid.uuid4, editable=False)
    
    def __str__(self):
        return f"{self.name} {self.uuid}"
    