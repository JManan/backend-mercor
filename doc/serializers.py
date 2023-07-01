from .models import Doc
from rest_framework import serializers

class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = ["name", "gender", "weight", "heigth", "phone_number", "email", "uuid"]