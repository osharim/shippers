# Generated by Django 2.0.13 on 2019-05-09 13:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0002_auto_20190509_0612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('status', models.CharField(blank=True, choices=[('VALIDATION_IN_PROCCESS', 'Validation in proccess'), ('VALIDATED', 'Validated'), ('SUSPENDED', 'Suspended')], default='VALIDATION_IN_PROCCESS', max_length=32, verbose_name='Status')),
                ('name', models.CharField(blank=True, max_length=256, verbose_name='Driver name')),
                ('surname', models.CharField(blank=True, max_length=256, verbose_name='Surname')),
                ('license_type', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], max_length=1, verbose_name='Licence type')),
                ('license_number', models.CharField(blank=True, max_length=20, verbose_name='Licence number')),
                ('license_expiration', models.DateField(blank=True, verbose_name='License exp')),
            ],
            options={
                'verbose_name': 'Operador',
                'verbose_name_plural': 'Operadores',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('status', models.CharField(blank=True, choices=[('VALIDATION_IN_PROCCESS', 'Validation in proccess'), ('VALIDATED', 'Validated'), ('SUSPENDED', 'Suspended')], default='VALIDATION_IN_PROCCESS', max_length=32, verbose_name='Status')),
                ('license_plate', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], max_length=8, verbose_name='Licence plate')),
                ('make', models.CharField(blank=True, max_length=128, verbose_name='Brand')),
                ('model_type', models.CharField(blank=True, max_length=128, verbose_name='Model type')),
                ('year', models.PositiveSmallIntegerField(blank=True, verbose_name='Year')),
                ('type', models.CharField(choices=[(0, 'Sin especificar'), (1, 'Camioneta de 1.5 toneladas'), (2, 'Camioneta de 3.5 toneladas'), (3, 'Camioneta de 5.5 toneladas'), (4, 'Rabón con caja seca'), (5, 'Rabón con caja refrigeradaTorton con caja seca'), (6, 'Torton con caja refrigerada'), (7, 'Trailer de 48ft con caja seca'), (8, 'Trailer de 48ft con caja refrigerada'), (9, 'Trailer de 53ft con caja seca'), (10, 'Trailer de 53ft con caja refrigerada')], max_length=1, verbose_name='Type vehicle')),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
            },
        ),
        migrations.AlterField(
            model_name='carrier',
            name='status',
            field=models.CharField(blank=True, choices=[('VALIDATION_IN_PROCCESS', 'Validation in proccess'), ('VALIDATED', 'Validated'), ('SUSPENDED', 'Suspended')], default='VALIDATION_IN_PROCCESS', max_length=32, verbose_name='Status'),
        ),
    ]