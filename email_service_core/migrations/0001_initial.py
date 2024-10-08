# Generated by Django 5.0.3 on 2024-08-28 08:51

import email_service_core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EmailSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email_name",
                    models.CharField(
                        choices=email_service_core.models.get_email_service_default_choices,
                        max_length=255,
                        unique=True,
                    ),
                ),
                ("email_list", models.TextField(blank=True, null=True)),
                ("enabled", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "EmailSetting",
                "verbose_name_plural": "EmailSettings",
            },
        ),
    ]
