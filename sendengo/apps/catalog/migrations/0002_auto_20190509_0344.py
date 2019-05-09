# Generated by Django 2.0.13 on 2019-05-09 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogrequirement',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.CatalogCategory', verbose_name='Category type'),
        ),
        migrations.AlterField(
            model_name='catalogrequirement',
            name='name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Name requirement'),
        ),
    ]