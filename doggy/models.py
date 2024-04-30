from django.db import models

# Create your models here.


class Breed(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(default=None)


class Temper(models.Model):
    type_temper = models.CharField(max_length=30)


class Address(models.Model):
    city = models.CharField(max_length=30)
    street_building = models.CharField(max_length=10)
    contact_phone = models.CharField(max_length=12)
    work_hours = models.CharField(max_length=20)


class Fur(models.Model):
    type_fur = models.CharField(max_length=15)


class Colour(models.Model):
    name = models.CharField(max_length=15)


class Medicament(models.Model):
    name = models.CharField(max_length=30)


class Vaccination(models.Model):
    name = models.ForeignKey(Medicament, on_delete=models.CASCADE, related_name='vaccination_name')
    date_created = models.DateTimeField(auto_now_add=True)


class Health(models.Model):
    state = models.BooleanField()
    vaccination = models.ManyToManyField(Vaccination, related_name='vaccination_case')
    parasite_treatment = models.BooleanField()


class Animal(models.Model):
    name = models.CharField(max_length=30)
    gender = models.BooleanField()
    date_of_birth = models.DateField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='animal_breed')
    weight = models.IntegerField()
    height = models.IntegerField()
    temper = models.ForeignKey(Temper, on_delete=models.CASCADE, related_name='animal_temper')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='animal_address')
    image = models.CharField(max_length=50)
    type_fur = models.ForeignKey(Fur, on_delete=models.CASCADE, related_name='animal_fur')
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE, related_name='animal_colour')
    life_story = models.TextField(max_length=500)
    health_state = models.ForeignKey(Health, on_delete=models.CASCADE, related_name='animal_health')
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


