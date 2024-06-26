from django.db import models


class Payer(models.Model):
    phone_area_code = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address_zip_code = models.CharField(max_length=10, blank=True, null=True)
    address_street_name = models.CharField(max_length=100, blank=True, null=True)
    address_street_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    identification_number = models.CharField(max_length=20, blank=True, null=True)
    identification_type = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_purchase = models.DateTimeField(blank=True, null=True)

class Item(models.Model):
    category_id = models.CharField(max_length=50, blank=True, null=True)
    currency_id = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

class Preference(models.Model):
    additional_info = models.TextField(blank=True, null=True)
    auto_return = models.CharField(max_length=200)
    back_url_failure = models.URLField()
    back_url_pending = models.URLField()
    back_url_success = models.URLField()
    binary_mode = models.BooleanField()
    client_id = models.CharField(max_length=200)
    collector_id = models.BigIntegerField()
    coupon_code = models.CharField(max_length=100, blank=True, null=True)
    coupon_labels = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField()
    date_of_expiration = models.DateTimeField(blank=True, null=True)
    expiration_date_from = models.DateTimeField(blank=True, null=True)
    expiration_date_to = models.DateTimeField(blank=True, null=True)
    expires = models.BooleanField()
    external_reference = models.CharField(max_length=200, blank=True, null=True)
    init_point = models.URLField()
    internal_metadata = models.JSONField(blank=True, null=True)
    marketplace = models.CharField(max_length=50)
    marketplace_fee = models.DecimalField(max_digits=10, decimal_places=2)
    metadata = models.JSONField(blank=True, null=True)
    notification_url = models.URLField(blank=True, null=True)
    operation_type = models.CharField(max_length=50)
    payer = models.OneToOneField(Payer, on_delete=models.CASCADE, related_name='preference')
    payment_methods = models.JSONField()
    processing_modes = models.JSONField(blank=True, null=True)
    product_id = models.CharField(max_length=50, blank=True, null=True)
    redirect_urls_failure = models.URLField(blank=True, null=True)
    redirect_urls_pending = models.URLField(blank=True, null=True)
    redirect_urls_success = models.URLField(blank=True, null=True)
    sandbox_init_point = models.URLField()
    site_id = models.CharField(max_length=10)
    shipments = models.JSONField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    financing_group = models.CharField(max_length=50, blank=True, null=True)
    items = models.ManyToManyField(Item)