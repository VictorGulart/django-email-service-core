import logging

from django.db import models
from django.conf import settings

logger = logging.getLogger(__name__)


def get_email_service_default_choices():
    app_name = "email_service_core"
    setting_name = "EMAIL_SERVICE_CORE_CONFIG"
    system_emails = "SystemEmails"

    # Check for main settings
    assert hasattr(settings, setting_name), (
        f"The '{setting_name}' setting is missing in your project settings. "
        f"This is required by the '{app_name}' app to provide default choices for the 'email_name' field. "
        "Please add this setting to your project settings."
    )

    # Check if the specific 'SystemEmails' choices are available within the main setting
    assert system_emails in settings.EMAIL_SERVICE_CORE_CONFIG, (
        f"The '{system_emails}' key is missing within the '{setting_name}' setting in your project settings. "
        f"This is required by the '{app_name}' app to provide default choices for the 'email_name' field. "
        "Please ensure this key is correctly configured."
    )
    return settings.EMAIL_SERVICE_CORE_CONFIG.get(
        "SystemEmails", models.TextChoices
    ).choices


class EmailSettingsManager(models.Manager):

    def get_or_none(self, email_name=""):
        return self.filter(email_name=email_name).first()


class EmailSettings(models.Model):

    email_name = models.CharField(
        max_length=255,
        choices=get_email_service_default_choices,
        null=False,
        unique=True,
    )
    email_list = models.TextField(null=True, blank=True)
    enabled = models.BooleanField(default=False)

    objects = EmailSettingsManager()

    class Meta:
        verbose_name = "EmailSetting"
        verbose_name_plural = "EmailSettings"

    def __str__(self):
        return self.email_name.replace("_", " ").title()
