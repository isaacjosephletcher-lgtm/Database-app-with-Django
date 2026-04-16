from django.contrib import admin
from .models import (
	Ability,
	Diagnosis,
	Employee,
	Invoice,
	LineItem,
	Observation,
	Owner,
	Patient,
	PatientAbility,
	Payment,
	ProcedureDefinition,
	Universe,
	Visit,
	VisitDiagnosis,
	VisitProcedure,
	CareNote,
)



@admin.register(Universe)
class UniverseAdmin(admin.ModelAdmin):
	list_display = ("universe_id", "name")
	search_fields = ("name",)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
	list_display = ("owner_id", "name", "phone", "email", "universe")
	search_fields = ("name", "phone", "email", "address")
	list_filter = ("universe",)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
	list_display = ("patient_id", "name", "owner", "universe", "dob", "color")
	search_fields = ("name", "color", "owner__name")
	list_filter = ("universe", "dob")
	date_hierarchy = "dob"


@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
	list_display = ("ability_id", "name", "ability_type")
	search_fields = ("name", "ability_type")
	list_filter = ("ability_type",)


@admin.register(PatientAbility)
class PatientAbilityAdmin(admin.ModelAdmin):
	list_display = ("patient_ability_id", "patient", "ability")
	search_fields = ("patient__name", "ability__name")
	list_filter = ("ability",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = (
		"employee_id",
		"name",
		"job_role",
		"specialty",
		"hire_date",
		"phone",
		"email",
	)
	search_fields = ("name", "job_role", "specialty", "phone", "email")
	list_filter = ("job_role", "specialty", "hire_date")
	date_hierarchy = "hire_date"


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
	list_display = ("diagnosis_id", "name", "code")
	search_fields = ("name", "code", "description")


@admin.register(ProcedureDefinition)
class ProcedureDefinitionAdmin(admin.ModelAdmin):
	list_display = ("procedure_id", "name", "standard_cost")
	search_fields = ("name", "description")


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
	list_display = ("visit_id", "patient", "vet", "start_at", "end_at", "reason")
	search_fields = ("patient__name", "vet__name", "reason")
	list_filter = ("start_at", "vet")
	date_hierarchy = "start_at"


@admin.register(VisitDiagnosis)
class VisitDiagnosisAdmin(admin.ModelAdmin):
	list_display = ("visit_diagnosis_id", "visit", "diagnosis", "employee", "recorded_at")
	search_fields = ("visit__patient__name", "diagnosis__name", "employee__name")
	list_filter = ("diagnosis", "employee", "recorded_at")
	date_hierarchy = "recorded_at"


@admin.register(VisitProcedure)
class VisitProcedureAdmin(admin.ModelAdmin):
	list_display = ("visit_procedure_id", "visit", "procedure", "employee", "performed_at")
	search_fields = ("visit__patient__name", "procedure__name", "employee__name")
	list_filter = ("procedure", "employee", "performed_at")
	date_hierarchy = "performed_at"


@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
	list_display = (
		"observation_id",
		"visit_procedure",
		"observation_type",
		"observed_value",
		"unit",
	)
	search_fields = ("observation_type", "description", "visit_procedure__visit__patient__name")
	list_filter = ("observation_type", "unit")


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
	list_display = ("invoice_id", "visit", "status", "issue_date", "due_date")
	search_fields = ("visit__patient__name", "status")
	list_filter = ("status", "issue_date", "due_date")
	date_hierarchy = "issue_date"


@admin.register(LineItem)
class LineItemAdmin(admin.ModelAdmin):
	list_display = (
		"line_item_id",
		"invoice",
		"line_item_type",
		"visit_procedure",
		"medication_id",
		"vaccination_id",
		"boarding_stay_id",
	)
	search_fields = ("line_item_type", "invoice__visit__patient__name")
	list_filter = ("line_item_type",)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
	list_display = ("payment_id", "invoice", "payment_date", "amount", "payment_method")
	search_fields = ("invoice__visit__patient__name", "payment_method")
	list_filter = ("payment_method", "payment_date")
	date_hierarchy = "payment_date"

@admin.register(CareNote)
class CareNoteAdmin(admin.ModelAdmin):
    list_display = ['patient', 'created_at', 'resolved', 'follow_up_date']
    list_filter = ['resolved']