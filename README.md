# Setup

=========================
django-email-service-core
=========================

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    ```py
    INSTALLED_APPS = [
        ...,
        "email_service_core",
    ]
    ```

## DECLARING EMAILS FOR AUTOMATIC CREATION

Each email setting has 3 values name, email comma separated list and enabled (bool)

```py
from ws.settings import SERVER_EMAIL

EMAIL_SETTINGS_CONFIG = [

    # WS APP
    ("SEND_CUSTOMER_ORDER_INVOICE", "technology@natoora.com,", True), # directly to customer or to technology
    ("SEND_CUSTOMER_ORDER_CREDIT_NOTE", "technology@natoora.com,", True),
    ("SEND_SUMMARY_EMAIL", "technology@natoora.com,", True),
    ("SEND_PRODUCT_HAS_NO_LOCATION", SERVER_MAIL, True),
    ("SEND_UNASSIGNED_ITEM_REPORT", "raph@natoora.com,carlos@natoora.com", True),
    ("SEND_USERS_EMAIL_NOTIFICATION", "", True), # specific user
    ("SEND_CSV_EXPORT", "", True), # specific user
    ("SEND_OPENEDI_NOTIFICATION_ISSUES", "keyaccounts@natoora.com,logs@natoora.com", True), 
    ("SEND_RETAIL_MISSING_PACKAGING", "technology@natoora.com,keyaccounts@natoora.com", True), 
    ("SEND_RETAIL_FINAL_CHECKS_ERRORS", SERVER_MAIL, True), 
    ("SEND_DAY_SPECIAL_PRICES_EXPIRATION", "wholesale@natoora.com", True), 
    ("SEND_EXCHANGE_RATE_EXPIRY", "franco@natoora.com,pablo@natoora.com", True), 
    ("SEND_WEBSOCKET_PICKINGSTAT_EXCEPTION", SERVER_MAIL, True), 
    ("SEND_HD_TEAM_CUSTOMER_DELETE_ACCOUNT_REQUEST", "clientsadmin@natoora.com, grocerydelivery@natoora.com", True), 
    ("SEND_HD_CUSTOMER_ACCOUNT_DELETION_CONFIRMATION", "", True), # directly to the customer
    ("SEND_HD_CUSTOMER_MESSAGES_TO_CUSTOMER_SERVICE", "homedelivery@natoora.com" or "grocerydelivery@natoora.com", True), # home delivery email for London otherwise grocery delivery email
    ("SEND_HD_CUSTOMER_ORDER_PRODUCT_DISABLED", "", True), # directly to user email
    ("SEND_HD_CUSTOMER_READY_TO_ORDER_UPDATE", "", True), # directly to user email
    ("SEND_HD_CUSTOMER_ORDER_CONFIRMATION", "", True), # user email

    # Suppliers MS
    ("send_supplier_created_email", "safety@natoora.com", True),
    ("send_supplier_reactivated_email", "safety@natoora.com", True),
    ("send_portal_user_activation_email", "", True), # directly to user
    ("send_portal_user_password_reset_email", "", True), # directly to user
    ("send_saq_status_change_email", "safety@natoora.com", True),
    ("send_expired_document_email", "safety@natoora.com", True),
    ("send_expiring_saq_email", "", True), # directly to user


    # Purchases MS

]
```


# Using email service on projects

## EmailSettings Manager

The manager has a get_or_none() function to facilitate the the getting of the object and to remove error handling as it's unnecessary.

## Check if email is enabled
```py 
from emailservice.models import EmailSettings

email_setting = EmailSettings.objects.get_or_none(email_name="order_invoice")

if not email_setting or not email_setting.enabled:
    logger.info(f"EmailSetting not enabled for ('order_invoice')")
    return
```

## Add email list
```py
from emailservice.models import EmailSettings
from app.sendmail import sendmail

email_setting = EmailSettings.objects.get(email_name="order_invoice")

sendmail(from="no-reply@natoora.com", to=email_setting.email_list)
```

# 