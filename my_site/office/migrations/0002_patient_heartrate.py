# Generated by Django 4.1.5 on 2023-02-24 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("office", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="heartrate",
            field=models.IntegerField(default=60),
        ),
    ]
