# Generated by Django 3.2.8 on 2021-11-08 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aeroreserve', '0006_alter_airlines_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentInfo',
        ),
    ]
