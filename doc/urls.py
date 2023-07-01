from django.contrib import admin
from django.urls import path, include
from doc import views as doc_views

urlpatterns = [
    path("", doc_views.index, name="index"),
    path("scrape/", doc_views.scrape, name="scrape")
]
