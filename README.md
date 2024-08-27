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
    ("order_confirmation", "", True), # user email
    ("order_invoice", "technology@natoora.com,", True), # directly to customer or to technology
    ("order_credit_note", "technology@natoora.com,", True),
    ("summary_email", "technology@natoora.com,", True),
    ("product_no_location", SERVER_MAIL, True),
    ("unassigned_item_service", "raph@natoora.com,carlos@natoora.com", True),
    ("user_forgot_password", "", True), # specific user
    ("send_users_notification", "", True), # specific user
    # CSVExport uses export types
    ("order_item_list", "", True), # specific user
    ("stock_totals", "", True), # specific user
    ("product_list", "", True), # specific user
    ("openedi_notification_issues", "keyaccounts@natoora.com,logs@natoora.com", True), 
    ("retail_invalid_packaging", "technology@natoora.com,keyaccounts@natoora.com", True), 
    ("retail_item_check_error", SERVER_MAIL, True), 
    ("specialprices_expiry", "wholesale@natoora.com", True), 
    ("exchange_rate_expiry", "franco@natoora.com,pablo@natoora.com", True), 
    ("websocket_pickingstat_exception", SERVER_MAIL, True), 
    ("supplier_created", "safety@natoora.com", True), 
    ("supplier_reactivated", "safety@natoora.com", True), 
    ("hd_team_customer_delete_account", "clientsadmin@natoora.com, grocerydelivery@natoora.com", True), 
    ("customer_request_delete_account", "", True), # directly to the customer
    ("customer_hd_app_messages", "homedelivery@natoora.com" or "grocerydelivery@natoora.com", True), # home delivery email for London otherwise grocery delivery email
    ("order_with_disabled_products", "", True), # directly to user email
    ("customer_ready_to_order", "", True), # directly to user email

    # Suppliers APP
    ("send_supplier_created_email", "safety@natoora.com", True),
    ("send_supplier_reactivated_email", "safety@natoora.com", True),
    ("send_portal_user_activation_email", "", True), # directly to user
    ("send_portal_user_password_reset_email", "", True), # directly to user
    ("send_saq_status_change_email", "safety@natoora.com", True),
    ("send_expired_document_email", "safety@natoora.com", True),
    ("send_expiring_saq_email", "", True), # directly to user
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