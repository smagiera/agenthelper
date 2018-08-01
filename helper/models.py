from django.db import models

# Create your models here.

class Vehicle(models.Model):
    OSOBOWY = "OS"
    CIEZAROWY = "CI"
    MOTOCYKL = "MO"
    PRZYCZEPA = "PR"
    CIAGNIK_ROLNICZY = "CR"
    CIAGNIK_SIODLOWY = "CS"
    AUTOBUS = "AU"
    TYPE_CHOICE = (
        (OSOBOWY, 'Osobowy'),
        (CIEZAROWY, 'Ciężarowy'),
        (MOTOCYKL, 'Motocykl'),
        (PRZYCZEPA, 'Przyczepa'),
        (CIAGNIK_ROLNICZY, 'Ciągnik rolniczy'),
        (CIAGNIK_SIODLOWY, 'Ciągnik siodłowy'),
        (AUTOBUS, 'Autobus')
    )
    vehicle_type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICE,
        default=OSOBOWY,
    )
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)
    vin = models.CharField(max_length=17)
    manufacture_year = models.IntegerField
    capacity = models.IntegerField
    power = models.IntegerField
    seats = models.IntegerField
    first_registered = models.DateField
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    leasing = models.ForeignKey(Leasing)

class Client(models.Model):
    name = models.CharField(max_length=100)
    pesel_or_regon = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
