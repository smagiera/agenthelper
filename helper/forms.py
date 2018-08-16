from django import forms
from django.forms import ModelForm
from .models import Policy, Vehicle, Client, Insurer
from dal import autocomplete

class PolicyForm(ModelForm):
    class Meta:
        model = Policy
        fields = [
        'number', 'client', 'date_start', 'date_end', 'date_issued', 'premium',
        'payment', 'installments', 'vehicle', 'insurer', 'scan1', 'scan2', 'scan3', 
        ]
        widgets = {
            'date_start': forms.DateInput(attrs={'class': 'datepicker'}),
            'date_end': forms.DateInput(attrs={'class': 'datepicker'}),
            'date_issued': forms.DateInput(attrs={'class': 'datepicker'}),
            'client': autocomplete.ModelSelect2(url='helper:client-autocomplete'),
            'vehicle': autocomplete.ModelSelect2(url='helper:vehicle-autocomplete'),
        }
        labels = {
            'number': 'Numer polisy',
            'client': 'Klient',
            'date_start': 'Data rozpoczęcia',
            'date_end': 'Data zakończenia',
            'date_issued': 'Data wystawienia',
            'premium': 'Składka',
            'payment': 'Płatność',
            'installments': 'Raty',
            'vehicle': 'Pojazd',
            'insurer': 'Towarzystwo',
            'scan1': 'Skan 1',
            'scan2': 'Skan 2',
            'scan3': 'Skan 3',
        }

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'vehicle_type', 'make', 'model', 'reg_number', 'vin',
            'manufacture_year', 'capacity', 'power', 'seats',
            'first_registered', 'owner',
        ]
        widgets = {
            'first_registered': forms.DateInput(attrs={'class': 'datepicker'}),
            'client': autocomplete.ModelSelect2(url='helper:client-autocomplete'),
        }
        labels = {
            'vehicle_type': 'Typ pojazdu',
            'make': 'Marka',
            'model': 'Model',
            'reg_number': 'Numer rejestracyjny',
            'manufacture_year': 'Rok produkcji',
            'capacity': 'Pojemność',
            'power': 'Moc(kW)',
            'seats': 'Liczba miejsc',
            'first_registered': 'Data pierwszej rejestracji',
            'owner': 'Właściciel',
        }

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = [
            'name', 'pesel_or_regon', 'address', 'phone_number', 'email',
        ]
        labels = {
            'name': 'Imię i nazwisko/Nazwa firmy',
            'pesel_or_regon': 'PESEL/REGON',
            'address': 'Adres',
            'phone_number': 'Numer telefonu',
        }

class InsurerForm(ModelForm):
    class Meta:
        model = Insurer
        fields = [ 'name']
        labels = { 'name': 'Nazwa Towarzystwa'}