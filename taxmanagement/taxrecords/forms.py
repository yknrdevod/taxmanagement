# taxrecords/forms.py
from django import forms
from .models import TaxRecord

class TaxRecordForm(forms.ModelForm):
    class Meta:
        model = TaxRecord
        fields = ('assessment_year', 'assessment_number', 'door_number', 'owner_name', 'relative_name', 'house_tax', 'library_cess', 'water_tax', 'lightning_tax', 'fire_tax', 'sports_cess', 'drainage_tax', 'total_current_year_tax', 'arrear_tax', 'total_tax', 'cluster_number', 'payment')