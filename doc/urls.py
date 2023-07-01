from django.contrib import admin
from django.urls import path, include
from doc import views as doc_views

urlpatterns = [
    path("scrape/", doc_views.scrape, name="scrape")
]
