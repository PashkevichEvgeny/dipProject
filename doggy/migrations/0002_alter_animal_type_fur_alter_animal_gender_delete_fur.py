# Generated by Django 5.0.4 on 2024-04-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doggy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='type_fur',
            field=models.IntegerField(choices=[(0, 'Long Haired'), (1, 'Middle Haired'), (2, 'Short Haired')], default=None),
        ),
        migrations.AlterField(
            model_name='animal',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Female'), (1, 'Male')], default=None),
        ),
        migrations.DeleteModel(
            name='Fur',
        ),
    ]
