from django.contrib import admin
from django.urls import path, include
from doc import views as doc_views
from patient import views as patient_views

urlpatterns = [
    path("", doc_views.index, name="index"),
    path("scrape/", doc_views.scrape, name="scrape"),
    path("doc/", doc_views.doc_data, name="doc-data"),
    path("patient/", patient_views.patient_data, name="patient-data")
]
