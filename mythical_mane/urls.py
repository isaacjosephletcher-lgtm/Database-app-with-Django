from django.urls import path
from . import views

app_name = "mythical_mane"

urlpatterns = [
    path("patients/", views.PatientListView.as_view(), name="patient_list"),
]
