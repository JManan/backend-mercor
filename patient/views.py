from django.shortcuts import render
from rest_framework import serializers
from .serializers import PatientSerializer
from .models import Patient
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def patient_data(request):
    if request.method == "POST":
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        uuid = request.query_params.get("id")
        try:
            patient = Patient.objects.get(uuid=uuid)
        except:
            patient= None
        serializer = PatientSerializer(patient)
        return JsonResponse(serializer.data)

# @api_view(["POST"])
# def add_patient(request):
#     serializer = PatientSerializer(data=request.data)
#     print(request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)