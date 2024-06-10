# Generated by Django 4.1.4 on 2024-06-10 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(blank=True, max_length=50, null=True)),
                ('currency_id', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Payer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_area_code', models.CharField(blank=True, max_length=10, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address_zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('address_street_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address_street_number', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('identification_number', models.CharField(blank=True, max_length=20, null=True)),
                ('identification_type', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('surname', models.CharField(blank=True, max_length=50, null=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_purchase', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('auto_return', models.CharField(max_length=200)),
                ('back_urls_failure', models.URLField()),
                ('back_urls_pending', models.URLField()),
                ('back_urls_success', models.URLField()),
                ('binary_mode', models.BooleanField()),
                ('client_id', models.CharField(max_length=200)),
                ('collector_id', models.BigIntegerField()),
                ('coupon_code', models.CharField(blank=True, max_length=100, null=True)),
                ('coupon_labels', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateTimeField()),
                ('date_of_expiration', models.DateTimeField(blank=True, null=True)),
                ('expiration_date_from', models.DateTimeField(blank=True, null=True)),
                ('expiration_date_to', models.DateTimeField(blank=True, null=True)),
                ('expires', models.BooleanField()),
                ('external_reference', models.CharField(blank=True, max_length=200, null=True)),
                ('init_point', models.URLField()),
                ('internal_metadata', models.JSONField(blank=True, null=True)),
                ('marketplace', models.CharField(max_length=50)),
                ('marketplace_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('notification_url', models.URLField(blank=True, null=True)),
                ('operation_type', models.CharField(max_length=50)),
                ('payment_methods', models.JSONField()),
                ('processing_modes', models.JSONField(blank=True, null=True)),
                ('product_id', models.CharField(blank=True, max_length=50, null=True)),
                ('redirect_urls_failure', models.URLField(blank=True, null=True)),
                ('redirect_urls_pending', models.URLField(blank=True, null=True)),
                ('redirect_urls_success', models.URLField(blank=True, null=True)),
                ('sandbox_init_point', models.URLField()),
                ('site_id', models.CharField(max_length=10)),
                ('shipments', models.JSONField(blank=True, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('financing_group', models.CharField(blank=True, max_length=50, null=True)),
                ('items', models.ManyToManyField(to='payment.item')),
                ('payer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preference', to='payment.payer')),
            ],
        ),
    ]