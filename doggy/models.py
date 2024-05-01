from django.db import models

# Create your models here.


class Breed(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(default=None)

    def __str__(self):
        return self.name


class Temper(models.Model):
    type_temper = models.CharField(max_length=30)

    def __str__(self):
        return self.type_temper


class Address(models.Model):
    name_shelter = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30)
    street_building = models.CharField(max_length=30)
    contact_phone = models.CharField(max_length=12)
    work_hours = models.CharField(max_length=20)

    def __str__(self):
        return self.name_shelter


class Colour(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Medicament(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Vaccination(models.Model):
    name = models.ForeignKey(Medicament, on_delete=models.CASCADE, related_name='vaccination_name')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Health(models.Model):
    class HealthState(models.IntegerChoices):
        UNKNOWN = 0
        HEALTHY = 1
        SICK = 2

    state = models.IntegerField(choices=HealthState, default=None)
    vaccination = models.ManyToManyField(Vaccination, related_name='vaccination_case')
    parasite_treatment = models.BooleanField()


class Animal(models.Model):
    class Gender(models.IntegerChoices):
        UNKNOWN = 0
        FEMALE = 1
        MALE = 2

    class Fur(models.IntegerChoices):
        UNKNOWN = 0
        LONG_HAIRED = 1
        MIDDLE_HAIRED = 2
        SHORT_HAIRED = 3

    name = models.CharField(max_length=30, blank=True)
    gender = models.IntegerField(choices=Gender, default=None)
    date_of_birth = models.DateField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='animal_breed')
    weight = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    temper = models.ForeignKey(Temper, on_delete=models.CASCADE, related_name='animal_temper')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='animal_address')
    image = models.ImageField(blank=True, default="media/default.png")
    type_fur = models.IntegerField(choices=Fur, default=None)
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE, related_name='animal_colour')
    life_story = models.TextField(max_length=500, blank=True)
    health_state = models.OneToOneField(Health, on_delete=models.CASCADE, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
