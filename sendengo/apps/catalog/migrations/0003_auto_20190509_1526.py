# Generated by Django 2.0.13 on 2019-05-09 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190509_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogrequirement',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.CatalogCategory', verbose_name='Category type'),
        ),
    ]
