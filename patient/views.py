from django.shortcuts import render
from rest_framework import serializers
from .serializers import PatientSerializer
from .models import Patient
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['GET'])
def patient_data(request):
    uuid = request.query_params.get("id")
    try:
        patient = Patient.objects.get(uuid=uuid)
    except:
        patient= None
    serializer = PatientSerializer(patient)
    return JsonResponse(serializer.data)