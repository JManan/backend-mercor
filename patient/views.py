from django.shortcuts import render
from rest_framework import serializers
from .serializers import PatientSerializer
from .models import Patient
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from doc.serializers import DocSerializer

@api_view(['GET', 'POST'])
def patient_data(request):
    if request.method == "POST":
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        short_uuid = request.query_params.get("id")
        try:
            patient = Patient.objects.get(short_uuid=short_uuid)
        except:
            patient= None
        serializer = PatientSerializer(patient)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def doc_list(request):
    id = request.query_params.get("id")
    patient = Patient.objects.get(short_uuid=id)
    docs = patient.doc.all()
    serializer = DocSerializer(docs, many=True)
    return JsonResponse(serializer.data, safe=False)
