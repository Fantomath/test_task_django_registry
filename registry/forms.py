from django import forms

from .models import RegistryRecord


class RegistryRecordForm(forms.ModelForm):
    class Meta:
        model = RegistryRecord
        fields = ["full_name", "birth_date", "credit_amount", "term_months"]
        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}),
        }
