from .models import Patient
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["name", "weight", "heigth", "gender", "phone_number", "email", "uuid", "address", "past_allergies", "past_operations", "past_treatment"]