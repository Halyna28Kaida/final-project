# Generated by Django 5.0.3 on 2024-04-15 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_buscket_total_summ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buscket',
            name='kids_quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
