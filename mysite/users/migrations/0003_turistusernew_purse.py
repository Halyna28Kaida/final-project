# Generated by Django 5.0.3 on 2024-04-27 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_turistusernew_purse'),
    ]

    operations = [
        migrations.AddField(
            model_name='turistusernew',
            name='purse',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]