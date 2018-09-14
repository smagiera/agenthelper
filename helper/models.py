from django.db import models
from django.urls import reverse


# Create your models here.

class Client(models.Model):
    class Meta:
        unique_together = ("name", "pesel_or_regon")
    name = models.CharField(max_length=100)
    pesel_or_regon = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100, blank=True)

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
    vin = models.CharField(max_length=17, unique=True)
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
    POLICY_TYPE_CHOICES = (
        (1, 'komunikacja'),
        (2, 'mieszkanie'),
        (3, 'firma'),
        (4, 'podróżne'),
        (5, 'życie')
    )
    number = models.CharField(max_length=20)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    policy_type = models.IntegerField(
        choices = POLICY_TYPE_CHOICES,
        default = 1,
    )
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
    policy_value = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    # for motor policies
    vehicle = models.ForeignKey(Vehicle, blank = True, null=True, on_delete=models.CASCADE)
    isTPL = models.BooleanField(default=False)
    isNNW = models.BooleanField(default=False)
    isAssistance = models.BooleanField(default=False)
    isCasco = models.BooleanField(default=False)
    # for property policies
    property = models.CharField(max_length=200, blank=True)
    isBuilding = models.BooleanField(default=False)
    isMovables = models.BooleanField(default=False)
    isElectronics = models.BooleanField(default=False)
    isAllRisk = models.BooleanField(default=False)

    scan1 = models.ImageField(blank=True)
    scan2 = models.ImageField(blank=True)
    scan3 = models.ImageField(blank=True)
    scan4 = models.ImageField(blank=True)
    scan5 = models.ImageField(blank=True)

    def get_absolute_url(self):
        return reverse('helper:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.number


