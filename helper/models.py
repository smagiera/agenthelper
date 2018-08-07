from django.db import models
from django.urls import reverse


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    pesel_or_regon = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('helper:client_details', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name

class Leasing(models.Model):
    name = models.CharField(max_length=100)
    regon = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Insurer(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    OSOBOWY = "Osobowy"
    CIEZAROWY = "Ciężarowy"
    MOTOCYKL = "Motocykl"
    PRZYCZEPA = "Przyczepa"
    CIAGNIK_ROLNICZY = "Ciągnik Rolniczy"
    CIAGNIK_SIODLOWY = "Ciągnik Siodłowy"
    AUTOBUS = "Autobus"
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
        max_length=16,
        choices=TYPE_CHOICE,
        default=OSOBOWY,
    )
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)
    vin = models.CharField(max_length=17)
    manufacture_year = models.IntegerField()
    capacity = models.IntegerField()
    power = models.IntegerField()
    seats = models.IntegerField()
    first_registered = models.DateField()
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    leasing = models.ForeignKey(Leasing, blank=True, null=True,
                                on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('helper:vehicle_details', kwargs={'pk': self.pk})
    
    def __str__(self):
        return " ".join([self.make, self.model, self.reg_number])

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
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_issued = models.DateField()
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
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    scan1 = models.ImageField(blank=True)
    scan2 = models.ImageField(blank=True)
    scan3 = models.ImageField(blank=True)

    def get_absolute_url(self):
        return reverse('helper:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.number



