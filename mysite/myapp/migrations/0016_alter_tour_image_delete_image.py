# Generated by Django 5.0.3 on 2024-04-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_image_alter_tour_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=models.ImageField(default=True, upload_to='images'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
