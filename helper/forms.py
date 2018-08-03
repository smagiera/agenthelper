from django import forms
from django.forms import ModelForm
from .models import Policy, Vehicle

class PolicyForm(ModelForm):
    class Meta:
        model = Policy
        fields = [
        'number', 'date_start', 'date_end', 'date_issued', 'premium',
        'payment', 'installments', 'vehicle', 'insurer', 
        ]
        widgets = {
            'date_start': forms.DateInput(attrs={'class': 'datepicker'}),
            'date_end': forms.DateInput(attrs={'class': 'datepicker'}),
            'date_issued': forms.DateInput(attrs={'class': 'datepicker'}),
        }

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'vehicle_type', 'make', 'model', 'reg_number', 'vin',
            'manufacture_year', 'capacity', 'power', 'seats',
            'first_registered', 'owner', 'leasing',
        ]
        widgets = {
            'first_registered': forms.DateInput(attrs={'class': 'datepicker'}),
        }