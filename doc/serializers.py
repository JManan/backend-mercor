from .models import Doc
from rest_framework import serializers

class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = ["name", "gender", "weight", "phone_number", "email", "uuid"]