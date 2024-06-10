from rest_framework import serializers
from .models import Preference, Payer, Item

class PayerSerializer(serializers.ModelSerializer):

    
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

    class Meta:
        model = Preference
        fields = '__all__'

    def create(self, validated_data):
        payer_data = validated_data.pop('payer')
        items_data = validated_data.pop('items')
        payer = Payer.objects.create(**payer_data)
        preference = Preference.objects.create(payer=payer, **validated_data)
        for item_data in items_data:
            item = Item.objects.create(**item_data)
            preference.items.add(item)
        return preference
