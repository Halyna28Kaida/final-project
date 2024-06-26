# Generated by Django 5.0.3 on 2024-04-06 13:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_tur_type_kind_tour_tour_type_kind_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='kids_quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='person_quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='prepayment',
        ),
        migrations.RemoveField(
            model_name='order',
            name='time',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_summ',
        ),
        migrations.RemoveField(
            model_name='order',
            name='tour',
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=50, null=True, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='order',
            name='is_paid',
            field=models.CharField(default=False, verbose_name='Оплачено'),
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=20, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_type_kind',
            field=models.IntegerField(choices=[(1, 'ЭКСКУРСИИ ПО ПРАГЕ'), (2, 'ЭКСКУРСИИ ПО ЧЕХИИ'), (3, 'ЭКСКУРСИИ ПО ЕВРОПЕ')], default=1),
        ),
        migrations.AlterModelTable(
            name='order',
            table='order',
        ),
        migrations.CreateModel(
            name='Buscket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('prepayment', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('person_quantity', models.PositiveIntegerField(blank=True)),
                ('kids_quantity', models.PositiveIntegerField(blank=True)),
                ('total_summ', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.tour')),
            ],
        ),
    ]
