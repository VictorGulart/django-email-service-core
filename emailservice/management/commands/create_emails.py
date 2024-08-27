from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from common.models import EmailSettings

CURRENTLY_AVAILABLE_EMAIL = [{}]


class Command(BaseCommand):
    help = "Create initial email settings"

    def add_arguments(self, parser):
        # Adding an optional argument
        parser.add_argument(
            "-e",
            "--email",
            type=str,
            help="Create target email settings.",
        )

        parser.add_argument(
            "-es",
            "--emails",
            nargs="*",
            type=str,
            help="Specify additional emails",
        )

    def handle(self, *args, **options):
        """
        SAFETY: does not update or create new one if the email setting already exists,
        it's on the user to edit these settings.

        list of emails in the system to create, if item is created then do nothing"""
        email = options["email"]
        emails = options["emails"]

        if email and emails:
            raise CommandError(
                "Either use --email or --emails arguments. Not both together."
            )

        # Create all email settings
