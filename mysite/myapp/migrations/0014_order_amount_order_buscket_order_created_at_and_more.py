# Generated by Django 5.0.3 on 2024-04-21 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_tour_place_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='buscket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.buscket'),
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_payment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='buscket',
            name='person_quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Оплачено'),
        ),
    ]