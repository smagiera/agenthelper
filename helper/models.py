from django.db import models
from datetime.date import today

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
        (AUTOBUS, 'Autobus'),
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
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

class Policy(models.Model):
    INSTALLMENTS_CHOICES = (
        (1, 'jedna'),
        (2, 'dwie'),
        (4, 'cztery'),
    )
    PAYMENT_CHOICES = (
        (1, 'gotówka'),
        (2, 'przelew')
    )
    number = models.CharField(max_length=20)
    date_issued = models.DateField(default=date.today)
    date_start = models.DateField()
    date_end = models.DateField()
    premium = models.DecimalField(max_digits=7, decimal_places=2)
    installments = models.IntegerField(
        choices = INSTALLMENTS_CHOICES,
        default=1,
    )
    payment = models.IntegerField(
        choices=PAYMENT_CHOICES,
        default=1,
    )
    insurer = models.ForeignKey(Insurer, on_delete=models.CASCADE)

class Insurer(models.Model):
    name = models.CharField(max_length=20)

