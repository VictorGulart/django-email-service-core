#!/usr/bin/env python

from django.db import models
import sys

sys.path.append("..")

from django.conf import settings

settings.configure(
    INSTALLED_APPS=["email_service_core"],
    ALLOWED_HOSTS=["localhost"],
    ROOT_URLCONF="urls",
    # uncomment when migrating
    # EMAIL_SERVICE_CORE_CONFIG={
    #     "SystemEmails": models.TextChoices
    # },
)

import django

django.setup()

from django.core.management import execute_from_command_line

execute_from_command_line(sys.argv)
