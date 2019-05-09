# Generated by Django 2.0.13 on 2019-05-09 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0006_auto_20190509_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrierrequirement',
            name='carrier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carrier.Carrier', verbose_name='Carrier'),
        ),
        migrations.AlterField(
            model_name='carrierrequirement',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.CatalogCategory', verbose_name='Category Requirement'),
        ),
        migrations.AlterField(
            model_name='carrierrequirement',
            name='requirement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.CatalogRequirement', verbose_name='Requirement'),
        ),
    ]