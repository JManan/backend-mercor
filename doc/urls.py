from django.contrib import admin
from django.urls import path, include
from doc import views as doc_views
from patient import views as patient_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", doc_views.index, name="index"),
    path("scrape/", doc_views.scrape, name="scrape"),
    path("doc/", doc_views.doc_data, name="doc-data"),
    path("add-doc/", doc_views.doc_data, name="doc-data"),
    path("patient/", patient_views.patient_data, name="list-patient"),
    path("add-patient/", patient_views.patient_data, name="add-patient"),
    path("patient-list/doc/", doc_views.patient_list, name="patient-list"),
    path("doc-list/patient/", patient_views.doc_list, name="doc-list"),
    path("patient/reports/", patient_views.patient_report, name="patient-report"),
    path("timeline/", patient_views.patient_timeline, name="patient-timeline")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                            document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()