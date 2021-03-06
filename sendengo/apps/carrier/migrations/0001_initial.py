# Generated by Django 2.0.13 on 2019-05-09 06:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0002_auto_20190509_0344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('company_name', models.CharField(blank=True, max_length=256, verbose_name='Company name')),
                ('owner_name', models.CharField(blank=True, max_length=256, verbose_name='Owner name')),
                ('owner_surname', models.CharField(blank=True, max_length=256, verbose_name='Owner surname')),
                ('address', models.CharField(blank=True, max_length=512, verbose_name='Address')),
                ('phone', models.CharField(blank=True, max_length=10, verbose_name='Phone')),
                ('email', models.CharField(blank=True, max_length=254, verbose_name='Email')),
                ('status', models.CharField(blank=True, choices=[('VALIDATION_IN_PROCCESS', 'Validation in proccess'), ('VALIDATED', 'Validated'), ('SUSPENDED', 'Suspended')], max_length=254, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Transportista',
                'verbose_name_plural': 'Transportistas',
            },
        ),
        migrations.CreateModel(
            name='CarrierRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('carrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrier.Carrier', verbose_name='Carrier')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.CatalogCategory', verbose_name='Category Requirement')),
                ('requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.CatalogRequirement', verbose_name='Requirement')),
            ],
            options={
                'verbose_name': 'Requerimiento',
                'verbose_name_plural': 'Requerimientos',
            },
        ),
    ]
