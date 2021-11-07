# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Airlines(models.Model):
    airline_id = models.IntegerField(primary_key=True)
    airline_name = models.CharField(max_length=45)
    arrival_time = models.TimeField(blank=True, null=True)
    departure_time = models.TimeField(blank=True, null=True)
    from_field = models.CharField(db_column='from', max_length=45, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=45, blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)
    datetravel = models.DateField(blank=True, null=True)
    fare = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AIRLINES'
        unique_together = (('airline_id', 'airline_name'),)


class Airport(models.Model):
    flight = models.OneToOneField(Airlines, models.DO_NOTHING, db_column='flight', primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    location = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AIRPORT'


class BookingDetails(models.Model):
    booking = models.OneToOneField('PassengerDetails', models.DO_NOTHING, primary_key=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    booked_seat = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    flight = models.CharField(max_length=45, blank=True, null=True)
    fare = models.ForeignKey('FlightCosts', models.DO_NOTHING, db_column='fare', blank=True, null=True)
    journey_date = models.DateField(db_column='journey_dATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOOKING_DETAILS'


class Destination(models.Model):
    from_field = models.CharField(db_column='from', primary_key=True, max_length=45)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=45, blank=True, null=True)
    arrival_time = models.TimeField()
    departure_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DESTINATION'
        unique_together = (('from_field', 'arrival_time'),)


class FlightCosts(models.Model):
    airline = models.OneToOneField(Airlines, models.DO_NOTHING, primary_key=True)
    fare = models.IntegerField()
    type = models.CharField(max_length=45, blank=True, null=True)
    airline_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FLIGHT_COSTS'
        unique_together = (('airline', 'fare'),)


class PassengerDetails(models.Model):
    passenger_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    seat_number = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    mobile_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PASSENGER_DETAILS'


class PaymentInfo(models.Model):
    passenger = models.OneToOneField(PassengerDetails, models.DO_NOTHING, primary_key=True)
    card_number = models.CharField(max_length=45, blank=True, null=True)
    card_type = models.CharField(max_length=45, blank=True, null=True)
    mobile_number = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PAYMENT_INFO'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
