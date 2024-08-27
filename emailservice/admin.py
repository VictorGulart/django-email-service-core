from django.contrib import admin

from emailservice.models import EmailSettings

# Register your models here.
@admin.register(EmailSettings)
class EmailSettingsAdmin(admin.ModelAdmin):
    """Email Settings Admin."""

    ...