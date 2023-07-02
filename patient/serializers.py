from .models import Patient, Report
from rest_framework import serializers
from doc.models import Doc

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class TimelineSerializer(serializers.ModelSerializer):
    doc_name = serializers.SerializerMethodField()

    def get_doc_name(self, object):
        doc = Doc.objects.get(short_uuid=object.doc_id.short_uuid)
        doc_name = doc.name
        return doc_name

    class Meta:
        model = Report
        fields = ["visit_name", "doc_name", "date", "time", "pdf_link"]