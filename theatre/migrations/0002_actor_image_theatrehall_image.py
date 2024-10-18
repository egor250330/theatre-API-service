# Generated by Django 5.1.2 on 2024-10-14 11:33

import theatre.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("theatre", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="actor",
            name="image",
            field=models.ImageField(
                null=True, upload_to=theatre.models.actor_image_path
            ),
        ),
        migrations.AddField(
            model_name="theatrehall",
            name="image",
            field=models.ImageField(
                null=True, upload_to=theatre.models.theatre_hall_image_path
            ),
        ),
    ]
