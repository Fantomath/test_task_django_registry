from django.urls import path

from . import views

app_name = "registry"

urlpatterns = [
    path("", views.registry_page, name="page"),
    path("delete/<int:record_id>/", views.delete_record, name="delete"),
]
