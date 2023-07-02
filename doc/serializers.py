from .models import Doc
from rest_framework import serializers

class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = '__all__'