from django.shortcuts import render
from django.views.generic import ListView
from .models import Patient


class PatientListView(ListView):
	model = Patient
	context_object_name = "patients"
	template_name = "mythical_mane/patient_list.html"
	paginate_by = 25

	def get_queryset(self):
		# Use select_related to fetch Owner and Universe in a single query
		return Patient.objects.select_related("owner", "universe").all()
