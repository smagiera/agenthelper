# Generated by Django 2.0.7 on 2018-08-03 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0004_auto_20180803_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(choices=[('Osobowy', 'Osobowy'), ('Ciężarowy', 'Ciężarowy'), ('Motocykl', 'Motocykl'), ('Przyczepa', 'Przyczepa'), ('Ciągnik Rolniczy', 'Ciągnik rolniczy'), ('Ciągnik Siodłowy', 'Ciągnik siodłowy'), ('Autobus', 'Autobus')], default='Osobowy', max_length=16),
        ),
    ]
