# Generated by Django 2.0.13 on 2019-05-09 02:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('name', models.CharField(blank=True, max_length=128, verbose_name='Name for this category e.g carrier documents, driver, vehicle')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='CatalogRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('name', models.CharField(blank=True, max_length=128, verbose_name='Name for this category')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.CatalogCategory', verbose_name='Select category type')),
            ],
            options={
                'verbose_name': 'Requerimiento',
                'verbose_name_plural': 'Requerimientos',
            },
        ),
    ]
