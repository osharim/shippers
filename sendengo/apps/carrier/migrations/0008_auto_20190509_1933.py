# Generated by Django 2.0.13 on 2019-05-09 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0007_auto_20190509_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='carrier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='carrier.Carrier', verbose_name='Carrier'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='carrier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='carrier.Carrier', verbose_name='Carrier'),
        ),
    ]