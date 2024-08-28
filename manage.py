#!/usr/bin/env python

import sys

sys.path.append("..")

from django.conf import settings

settings.configure(
    INSTALLED_APPS=["email_service_core"],
    ALLOWED_HOSTS=["localhost"],
    ROOT_URLCONF="urls",
    # EMAIL_SERVICE_CORE_CONFIG={"choices": []},  # uncomment when migrating
)

import django

django.setup()

from django.core.management import execute_from_command_line

execute_from_command_line(sys.argv)
