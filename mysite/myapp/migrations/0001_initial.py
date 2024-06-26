# Generated by Django 5.0.3 on 2024-03-30 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('prepayment', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('person_quantity', models.PositiveIntegerField(blank=True)),
                ('kids_quantity', models.PositiveIntegerField(blank=True)),
                ('total_summ', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('duration', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('beginning', models.TimeField()),
                ('meeting_place', models.CharField(blank=True, max_length=300, null=True)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('tour_type', models.IntegerField(choices=[(1, 'ИНДИВИДУАЛЬНЫЕ ЭКСКУРСИИ'), (2, 'ГРУППОВЫЕ ЭКСКУРСИИ')], default=1)),
                ('monday', models.BooleanField(default=True)),
                ('tuesday', models.BooleanField(default=True)),
                ('wednesday', models.BooleanField(default=True)),
                ('thursday', models.BooleanField(default=True)),
                ('friday', models.BooleanField(default=True)),
                ('saturday', models.BooleanField(default=True)),
                ('sunday', models.BooleanField(default=True)),
                ('kids_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('adult_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('tur_type_kind', models.IntegerField(choices=[(1, 'ЄКСКУРСИИ ПО ПРАГЕ'), (2, 'ЄКСКУРСИИ ПО ЧЕХИИ'), (3, 'ЄКСКУРСИИ ПО ЕВРОПЕ')], default=1)),
            ],
        ),
    ]
