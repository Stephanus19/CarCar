# Generated by Django 4.0.3 on 2023-01-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='vin',
            field=models.CharField(max_length=17, unique=True),
        ),
        migrations.AlterField(
            model_name='technician',
            name='employee_number',
            field=models.BigIntegerField(null=True, unique=True),
        ),
    ]