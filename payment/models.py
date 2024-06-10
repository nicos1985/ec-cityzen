from django.db import models
from django.core.exceptions import ValidationError

def validate_back_urls(back_urls):
    if not isinstance(back_urls, dict):
        raise ValidationError('Field must be an dictionary.')
    required_keys = {'failure', 'pending', 'success'}
    if set(back_urls.keys()) != required_keys:
        raise ValidationError(f'The dictionary must have this keys: {required_keys}')
    for key, value in back_urls.items():
        if not isinstance(value, str):
            raise ValidationError(f'The value for {key} must be of type string')
    


# Create your models here.
class PreferenceMP(models.Model):
    additional_info = models.CharField(max_length=250, null=True)
    auto_return = models.CharField(max_length=100, null=True)
    back_urls = models.JSONField(validators=[validate_back_urls])
    binary_mode = models.BooleanField()
    client_id = models.CharField(max_length=30)
    collector_id = models.CharField(max_length=30)
    coupon_code = models.CharField(max_length=100, null=True)
    coupon_labels = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField()
    date_of_expiration = models.DateTimeField(null=True)
    expiration_date_from =  models.DateTimeField(null=True)
    expiration_date_to = models.DateTimeField(null=True)
    expires = models.BooleanField()
    external_reference = models.CharField(max_length=100, null=True)
    id_preference = models.CharField(max_length=100)
    init_point = models.CharField(max_length=300)
    internal_metadata = models.CharField(max_length=300, null=True)
    items = models.JSONField()
    marketplace = models.CharField(max_length=100, null=True)
    marketplace_fee = models.IntegerField()
    metadata = models.JSONField()
    notification_url = models.CharField(max_length=500, null=True)
    operation_type = models.CharField(max_length=100, null=True)
    payer = models.ForeignKey(PayerMP, on_delete=models.CASCADE )
    payment_methods = models.ForeignKey(PaymentsMethodsMP, on_delete=models.CASCADE)
    processing_modes = models.CharField(max_length=500, null=True)
    product_id = models.CharField(max_length=100, null=True)
    redirect_urls = models.JSONField(validators=[validate_back_urls], null=True)
    sandbox_init_point = models.CharField(max_length=500, null=True)
    site_id = models.CharField(max_length=100, null=True)
    shipments = models.JSONField()
    total_amount = models.CharField(max_length=100, null=True)
    last_updated = models.CharField(max_length=100, null=True)
    financing_group = models.CharField(max_length=100, null=True)



    class PayerMP(models.Model):
        pass

    class PaymentsMethodsMP(models.Model):
        pass