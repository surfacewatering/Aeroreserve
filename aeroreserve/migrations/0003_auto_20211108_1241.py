# Generated by Django 3.2.8 on 2021-11-08 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aeroreserve', '0002_passenger'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassengerTicketRel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('JDate', models.DateField()),
                ('PNR', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Date_of_booking', models.DateField()),
                ('fk_flights', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aeroreserve.airlines')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Airport',
        ),
        migrations.AddField(
            model_name='passengerticketrel',
            name='PNR',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aeroreserve.ticket'),
        ),
        migrations.AddField(
            model_name='passengerticketrel',
            name='SSN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aeroreserve.passenger'),
        ),
        migrations.AlterUniqueTogether(
            name='passengerticketrel',
            unique_together={('PNR', 'SSN')},
        ),
    ]
