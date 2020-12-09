# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BanType(models.Model):
    id = models.SmallAutoField(primary_key=True)
    ban_type = models.CharField(max_length=20, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'ban_type'


class BantypeFueltype(models.Model):
    marka = models.SmallIntegerField(blank=True, null=True)
    model = models.SmallIntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    engine = models.IntegerField(blank=True, null=True)
    gearbox = models.SmallIntegerField(blank=True, null=True)
    transmission = models.SmallIntegerField(blank=True, null=True)
    ban_type = models.SmallIntegerField(blank=True, null=True)
    fuel_type_id = models.SmallIntegerField(blank=True, null=True)
    fuel_type = models.CharField(max_length=10, blank=True, null=True)
    objects = models.Manager()

    # def __str__(self):
    #     return self.fuel_type

    class Meta:
        managed = False
        db_table = 'bantype_fueltype'


class Car(models.Model):
    id = models.BigAutoField(primary_key=True)
    marka = models.ForeignKey('Marka', models.DO_NOTHING, db_column='marka', blank=True, null=True)
    model = models.ForeignKey('Model', models.DO_NOTHING, db_column='model', blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    currency = models.ForeignKey('Currency', models.DO_NOTHING, db_column='currency', blank=True, null=True)
    unique_id = models.IntegerField(unique=True, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    city = models.ForeignKey('City', models.DO_NOTHING, db_column='city', blank=True, null=True)
    engine = models.CharField(max_length=5, blank=True, null=True)
    fuel_type = models.ForeignKey('FuelType', models.DO_NOTHING, db_column='fuel_type', blank=True, null=True)
    ban_type = models.ForeignKey(BanType, models.DO_NOTHING, db_column='ban_type', blank=True, null=True)
    color = models.ForeignKey('Color', models.DO_NOTHING, db_column='color', blank=True, null=True)
    used_by_km = models.IntegerField(blank=True, null=True)
    engine_power = models.SmallIntegerField(blank=True, null=True)
    transmission = models.SmallIntegerField(blank=True, null=True)
    gearbox = models.ForeignKey('Gearbox', models.DO_NOTHING, db_column='gearbox', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    loan = models.SmallIntegerField(blank=True, null=True)
    barter = models.SmallIntegerField(blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    new = models.SmallIntegerField(blank=True, null=True)
    is_indexed = models.SmallIntegerField(blank=True, null=True)
    is_parsed = models.SmallIntegerField(blank=True, null=True)
    request_count = models.SmallIntegerField(blank=True, null=True)
    seller = models.ForeignKey('Seller', models.DO_NOTHING, db_column='seller', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car'


class CarModified(models.Model):
    id = models.BigIntegerField(primary_key=True)
    marka = models.SmallIntegerField(blank=True, null=True)
    model = models.SmallIntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    currency = models.SmallIntegerField(blank=True, null=True)
    unique_id = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    city = models.SmallIntegerField(blank=True, null=True)
    engine = models.IntegerField(blank=True, null=True)
    fuel_type = models.SmallIntegerField(blank=True, null=True)
    ban_type = models.SmallIntegerField(blank=True, null=True)
    color = models.SmallIntegerField(blank=True, null=True)
    used_by_km = models.IntegerField(blank=True, null=True)
    engine_power = models.SmallIntegerField(blank=True, null=True)
    transmission = models.SmallIntegerField(blank=True, null=True)
    gearbox = models.SmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    loan = models.SmallIntegerField(blank=True, null=True)
    barter = models.SmallIntegerField(blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    new = models.SmallIntegerField(blank=True, null=True)
    is_indexed = models.SmallIntegerField(blank=True, null=True)
    is_parsed = models.SmallIntegerField(blank=True, null=True)
    request_count = models.SmallIntegerField(blank=True, null=True)
    seller = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_modified'


class CascadedCar(models.Model):
    id = models.BigIntegerField(primary_key=True)
    marka = models.SmallIntegerField(blank=True, null=True)
    model = models.SmallIntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    engine = models.IntegerField(blank=True, null=True)
    gearbox = models.SmallIntegerField(blank=True, null=True)
    transmission = models.SmallIntegerField(blank=True, null=True)
    ban_type = models.SmallIntegerField(blank=True, null=True)
    fuel_type = models.SmallIntegerField(blank=True, null=True)
    used_by_km = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    currency = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cascaded_car'


class City(models.Model):
    id = models.SmallAutoField(primary_key=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class Color(models.Model):
    id = models.SmallAutoField(primary_key=True)
    color = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'color'


class Currency(models.Model):
    id = models.SmallAutoField(primary_key=True)
    currency = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currency'


class Details(models.Model):
    id = models.BigAutoField(primary_key=True)
    details = models.ForeignKey('UniqueDetails', models.DO_NOTHING, db_column='details', blank=True, null=True)
    car = models.ForeignKey(Car, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'details'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Engine(models.Model):
    engine = models.CharField(max_length=5, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'engine'


class EngineGearbox(models.Model):
    marka = models.SmallIntegerField(blank=True, null=True)
    model = models.SmallIntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    engine = models.IntegerField(blank=True, null=True)
    gearbox_id = models.SmallIntegerField(blank=True, null=True)
    gearbox = models.CharField(max_length=20, blank=True, null=True)
    objects = models.Manager()

    # def __str__(self):
    #     return self.gearbox

    class Meta:
        managed = False
        db_table = 'engine_gearbox'


class FuelType(models.Model):
    id = models.SmallAutoField(primary_key=True)
    fuel_type = models.CharField(max_length=10, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'fuel_type'


class Gearbox(models.Model):
    id = models.SmallAutoField(primary_key=True)
    gearbox = models.CharField(max_length=20, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'gearbox'


class GearboxTransmission(models.Model):
    marka = models.SmallIntegerField(blank=True, null=True)
    model = models.SmallIntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    engine = models.IntegerField(blank=True, null=True)
    gearbox = models.SmallIntegerField(blank=True, null=True)
    transmission_id = models.SmallIntegerField(blank=True, null=True)
    transmission = models.CharField(max_length=6, blank=True, null=True)
    objects = models.Manager()


    class Meta:
        managed = False
        db_table = 'gearbox_transmission'


class Images(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(unique=True, max_length=200, blank=True, null=True)
    is_main = models.SmallIntegerField(blank=True, null=True)
    car = models.ForeignKey(Car, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'


class Keywords(models.Model):
    keyword = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keywords'


class Logs(models.Model):
    id = models.BigAutoField(primary_key=True)
    link = models.CharField(max_length=100, blank=True, null=True)
    exception_info = models.TextField(blank=True, null=True)
    traceback_info = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs'


class Marka(models.Model):
    id = models.SmallAutoField(primary_key=True)
    marka = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.marka

    class Meta:
        managed = False
        db_table = 'marka'


class MarkaModel(models.Model):
    id = models.SmallAutoField(primary_key=True)
    marka = models.IntegerField(blank=True, null=True)
    model_id = models.SmallIntegerField(blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'test'


class Model(models.Model):
    id = models.SmallAutoField(primary_key=True)
    model = models.CharField(max_length=100, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'model'


class ModelYear(models.Model):
    marka = models.SmallIntegerField(blank=True, null=True)
    model = models.SmallIntegerField(blank=True, null=True)
    year_id = models.IntegerField(blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    objects = models.Manager()


    class Meta:
        managed = False
        db_table = 'model_year'


class PhoneNumber(models.Model):
    id = models.BigAutoField(primary_key=True)
    phone_number = models.ForeignKey('UniquePhoneNumber', models.DO_NOTHING, db_column='phone_number', blank=True, null=True)
    car = models.ForeignKey(Car, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone_number'


class Requirements(models.Model):
    id = models.SmallAutoField(primary_key=True)
    min_year = models.SmallIntegerField(blank=True, null=True)
    max_year = models.SmallIntegerField(blank=True, null=True)
    min_price = models.IntegerField(blank=True, null=True)
    max_price = models.IntegerField(blank=True, null=True)
    marka = models.ForeignKey(Marka, models.DO_NOTHING, db_column='marka')
    model = models.ForeignKey(Model, models.DO_NOTHING, db_column='model')
    engine = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirements'


class RequirementsBanType(models.Model):
    requirement = models.ForeignKey(Requirements, models.DO_NOTHING, blank=True, null=True)
    ban_type = models.ForeignKey(BanType, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirements_ban_type'


class RequirementsDetails(models.Model):
    requirement = models.ForeignKey(Requirements, models.DO_NOTHING, blank=True, null=True)
    details = models.ForeignKey('UniqueDetails', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirements_details'


class RequirementsFuelType(models.Model):
    requirement = models.ForeignKey(Requirements, models.DO_NOTHING, blank=True, null=True)
    fuel_type = models.ForeignKey(FuelType, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirements_fuel_type'


class RequirementsGearbox(models.Model):
    requirement = models.ForeignKey(Requirements, models.DO_NOTHING, blank=True, null=True)
    gearbox = models.ForeignKey(Gearbox, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirements_gearbox'


class RequirementsKeywords(models.Model):
    id = models.BigAutoField(primary_key=True)
    requirement = models.ForeignKey(Requirements, models.DO_NOTHING, blank=True, null=True)
    keyword = models.ForeignKey(Keywords, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirements_keywords'


class Seller(models.Model):
    id = models.BigAutoField(primary_key=True)
    seller = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seller'


class Transmission(models.Model):
    id = models.SmallAutoField(primary_key=True)
    transmission = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return self.transmission

    class Meta:
        managed = False
        db_table = 'transmission'


class TransmissionBantype(models.Model):
    marka = models.SmallIntegerField(blank=True, null=True)
    model = models.SmallIntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    engine = models.IntegerField(blank=True, null=True)
    gearbox = models.SmallIntegerField(blank=True, null=True)
    transmission = models.SmallIntegerField(blank=True, null=True)
    ban_type_id = models.SmallIntegerField(blank=True, null=True)
    ban_type = models.CharField(max_length=20, blank=True, null=True)
    objects = models.Manager()
    def __str__(self):
        return self.ban_type

    class Meta:
        managed = False
        db_table = 'transmission_bantype'


class UniqueDetails(models.Model):
    id = models.SmallAutoField(primary_key=True)
    unique_details = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unique_details'


class UniquePhoneNumber(models.Model):
    id = models.BigAutoField(primary_key=True)
    unique_phone_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unique_phone_number'


class Year(models.Model):
    year = models.SmallIntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'year'


class YearEngine(models.Model):
    marka = models.SmallIntegerField(blank=True, null=True)
    model = models.SmallIntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    engine_id = models.IntegerField(blank=True, null=True)
    engine = models.CharField(max_length=5, blank=True, null=True)
    objects = models.Manager()


    class Meta:
        managed = False
        db_table = 'year_engine'


class car_information(models.Model):
    id = models.AutoField(primary_key=True)
    marka = models.ForeignKey(Marka, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(MarkaModel, on_delete=models.SET_NULL, null=True)
    year = models.ForeignKey(ModelYear, on_delete=models.SET_NULL, null=True)
    engine = models.ForeignKey(YearEngine, on_delete=models.SET_NULL, null=True)
    # gearbox = models.ForeignKey(EngineGearbox, on_delete=models.SET_NULL, null=True)
    #transmission = models.ForeignKey(GearboxTransmission, on_delete=models.SET_NULL, null=True)
    #ban_type = models.ForeignKey(TransmissionBantype, on_delete=models.SET_NULL, null=True)
    #fuel_type = models.ForeignKey(BantypeFueltype, on_delete=models.SET_NULL, null=True)
    #used_by_km = models.IntegerField(blank=True, null=True)
    objects = models.Manager()


class car_filtering_logs(models.Model):
    id = models.AutoField(primary_key=True)
    marka = models.ForeignKey(Marka, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(MarkaModel, on_delete=models.SET_NULL, null=True)
    year = models.ForeignKey(ModelYear, on_delete=models.SET_NULL, null=True)
    engine = models.ForeignKey(YearEngine, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()



class car_information_details(models.Model):
    id = models.AutoField(primary_key=True)
    car_information = models.ForeignKey(car_information, on_delete=models.SET_NULL, null=True)
    COLOR_CHOICES = ((0, 'Gümüşü'), (1, 'Boz'), (2, 'Yaş Asfalt'), (3, 'Göy'), (4, 'Tünd qırmızı'), (5, 'Qara'), (6, 'Ağ'))
    SPARE_PARTS_CHOICES = ((0, 'Dəyişdirilib'), (1, 'Rəng'), (2, 'Qəzasız'))
    ALLOY_WHEELS_CHOICES = ((0, '18'), (1, '16'), (2, 'yox'))
    OPTIONS_CHOICES = ((0, 'Var'), (1, 'Yox'))

    alloy_wheels = models.SmallIntegerField(choices=ALLOY_WHEELS_CHOICES, null=True)
    luke = models.SmallIntegerField(choices=OPTIONS_CHOICES, null=True)
    leather_salon = models.SmallIntegerField(choices=OPTIONS_CHOICES, null=True)
    start_stop= models.SmallIntegerField(choices=OPTIONS_CHOICES, null=True)
    monitor = models.SmallIntegerField(choices=OPTIONS_CHOICES, null=True)

    front_bumper = models.SmallIntegerField(choices=SPARE_PARTS_CHOICES, null=True)
    front_hood = models.SmallIntegerField(choices=SPARE_PARTS_CHOICES, null=True)
    front_right_corner = models.SmallIntegerField(choices=SPARE_PARTS_CHOICES, null=True)
    front_left_corner = models.SmallIntegerField(choices=SPARE_PARTS_CHOICES, null=True)
    front_right_door = models.SmallIntegerField(choices=SPARE_PARTS_CHOICES, null=True)
    front_left_door = models.SmallIntegerField(choices=SPARE_PARTS_CHOICES, null=True)
    dam = models.SmallIntegerField(choices=SPARE_PARTS_CHOICES, null=True)
    back_left_door = models.SmallIntegerField(choices=SPARE_PARTS_CHOICES, null=True)
    back_right_door = models.SmallIntegerField(choices=SPARE_PARTS_CHOICES, null=True)
    back_right_corner = models.SmallIntegerField(choices=SPARE_PARTS_CHOICES, null=True)
    back_left_corner = models.SmallIntegerField(choices=SPARE_PARTS_CHOICES, null=True)
    begaj = models.SmallIntegerField(choices=SPARE_PARTS_CHOICES, null=True)
    back_bumper = models.SmallIntegerField(choices=SPARE_PARTS_CHOICES, null=True)
    right_pole = models.SmallIntegerField(choices=SPARE_PARTS_CHOICES, null=True)
    left_pole = models.SmallIntegerField(choices=SPARE_PARTS_CHOICES, null=True)


    color = models.SmallIntegerField(choices=COLOR_CHOICES, null=True)

