from django import forms
from django.forms import ModelForm
from .models import Policy

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