# django-email-service-core
---------------------------

Quick start
-----------

1. Add "email_service_core" to your INSTALLED_APPS setting like this::

    ```py
    INSTALLED_APPS = [
        ...,
        "email_service_core",
    ]
    ```

# Using email service on projects

## Project Settings 

It is necessary to define the email choices available in the system, this way we can handle them in one place.
The Email Service will be looking exactly for ```EMAIL_SERVICE_CORE_CONFIG``` in the project settings, with a key 
with ```SystemEmail``` which is a Django ```models.TextChoices```.

Example:

```py

from django.db import models

class SystemEmails(models.TextChoices):
    SEND_CUSTOMER_ORDER_INVOICE = ("Send Customer Order Invoice", "SEND_CUSTOMER_ORDER_INVOICE")

EMAIL_SERVICE_CORE_CONFIG = {"SystemEmails": SystemEmails}

```

## EmailSettings Manager

The manager has a ```get_or_none()``` function to facilitate the fetch object and to remove error handling as it's unnecessary.

It's recommended to add a logger info to make sure that the system is aware of the email not being enabled or set. 

## Check if email is enabled
```py 
from emailservice.models import EmailSettings
from app.settings import SystemEmails


email_setting = EmailSettings.objects.get_or_none(email_name=SystemEmails.SEND_CUSTOMER_ORDER_INVOICE)

if not email_setting or not email_setting.enabled:
    logger.info(f"EmailSetting not enabled for ('{SystemEmails.SEND_CUSTOMER_ORDER_INVOICE}') on funciton x().")
    return

```

## Sending to specified email list
```py
from emailservice.models import EmailSettings
from app.settings import SystemEmails

email_setting = EmailSettings.objects.get_or_none(email_name=SystemEmails.SEND_CUSTOMER_ORDER_INVOICE)

sendmail(from="no-reply@natoora.com", to=email_setting.email_list)
```

# 