from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid

class Doc(models.Model):
    name = models.TextField()
    phone_number = PhoneNumberField(blank=True)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    uuid = models.UUIDField(primary_key=True, unique=True,default = uuid.uuid4, editable=False)
    short_uuid = models.CharField(max_length=10, blank=True, editable=False)
    location = models.TextField()
    working_hrs = models.TextField()
    designation = models.CharField(max_length=30)
    short_uuid = models.CharField(max_length=10, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.short_uuid:
            self.short_uuid = str(self.uuid)[:10]
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} {self.short_uuid}"
    