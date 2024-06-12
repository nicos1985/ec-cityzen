from rest_framework import serializers
from .models import Preference, Payer, Item

class BackUrlsSerializer(serializers.Serializer):
    failure = serializers.URLField()
    pending = serializers.URLField()
    success = serializers.URLField()



class PayerSerializer(serializers.ModelSerializer):

    date_created = serializers.DateTimeField(allow_null=True, required=False)
    last_purchase = serializers.DateTimeField(allow_null=True, required=False)

    class Meta:
        model = Payer
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'

class PreferenceSerializer(serializers.ModelSerializer):
    payer = PayerSerializer()
    items = ItemSerializer(many=True)
    date_created = serializers.DateTimeField(allow_null=True, required=False)
    date_of_expiration = serializers.DateTimeField(allow_null=True, required=False)
    expiration_date_from = serializers.DateTimeField(allow_null=True, required=False)
    expiration_date_to = serializers.DateTimeField(allow_null=True, required=False)
    last_updated = serializers.DateTimeField(allow_null=True, required=False)
    back_urls = BackUrlsSerializer(write_only=True)
    back_url_failure = serializers.URLField(read_only=True)
    back_url_pending = serializers.URLField(read_only=True)
    back_url_success = serializers.URLField(read_only=True)
    class Meta:
        model = Preference
        fields = '__all__'

    def create(self, validated_data):
        #Trabajar diccionarios anidados de payer
        payer_data = validated_data.pop('payer')
        print(f'payer_data: {payer_data}')
        payer_validated_phone = payer_data.pop('phone')
        validated_data['phone_area_code'] = payer_validated_phone['area_code']
        validated_data['phone_number'] = payer_data['phone']['number']
        validated_data['address_zip_code'] = payer_data['address']['zip_code']
        validated_data['address_street_name'] = payer_data['address']['street_name']
        validated_data['address_street_number'] = payer_data['address']['street_number']
        validated_data['identification_number'] = payer_data['identification']['number']
        validated_data['identification_type'] = payer_data['identification']['type']
        payer = Payer.objects.create(**payer_data)
        
        #Trabajar diccionarios anidados de back_urls
        back_urls_data = validated_data.pop('back_urls')
        validated_data['back_url_failure'] = back_urls_data['failure']
        validated_data['back_url_pending'] = back_urls_data['pending']
        validated_data['back_url_success'] = back_urls_data['success']
        #crear la preferencia
        preference = Preference.objects.create(payer=payer, **validated_data)
        #Crear los items
        items_data = validated_data.pop('items')
        for item_data in items_data:
            item = Item.objects.create(**item_data)
            preference.items.add(item)
        return preference
