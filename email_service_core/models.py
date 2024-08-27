import logging

from django.db import models
from django.conf import settings

logger = logging.getLogger(__name__)


def get_email_service_default_choices():
    assert hasattr(
        settings, "EMAIL_SERVICE_CORE_CONFIG"
    ), "Project settings must override the EMAIL_SERVICE_CORE_CONFIG attribute."
    return settings.EMAIL_SERVICE_CORE_CONFIG.get("choices", [])


class EmailSettingsManager(models.Manager):

    def get_or_none(self, email_name=""):
        return self.filter(email_name=email_name).first()


class EmailSettings(models.Model):

    email_name = models.CharField(
        max_length=255, choices=get_email_service_default_choices, null=False
    )
    email_list = models.TextField(null=True, blank=True)
    enabled = models.BooleanField(default=False)

    objects = EmailSettingsManager()

    class Meta:
        verbose_name = "EmailSetting"
        verbose_name_plural = "EmailSettings"

    def __str__(self):
        return self.email_name.replace("_", " ").title()
