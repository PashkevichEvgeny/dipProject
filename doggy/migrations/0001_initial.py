# Generated by Django 5.0.4 on 2024-04-30 09:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('street_building', models.CharField(max_length=10)),
                ('contact_phone', models.CharField(max_length=12)),
                ('work_hours', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Fur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_fur', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField()),
                ('parasite_treatment', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Temper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_temper', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.BooleanField()),
                ('date_of_birth', models.DateField()),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('image', models.CharField(max_length=50)),
                ('life_story', models.TextField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal_address', to='doggy.address')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal_breed', to='doggy.breed')),
                ('colour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal_colour', to='doggy.colour')),
                ('type_fur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal_fur', to='doggy.fur')),
                ('health_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal_health', to='doggy.health')),
                ('temper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal_temper', to='doggy.temper')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccination_name', to='doggy.medicament')),
            ],
        ),
        migrations.AddField(
            model_name='health',
            name='vaccination',
            field=models.ManyToManyField(related_name='vaccination_case', to='doggy.vaccination'),
        ),
    ]
