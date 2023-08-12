from rest_framework import serializers

from core.models import Buyer, Pan


class PanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pan
        fields = '__all__'


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ["email", "password"]

    def create(self, validated_data):
        buyer = super(BuyerSerializer, self).create(validated_data)
        buyer.set_password(buyer.password)
        buyer.is_active = True
        buyer.save()
        return buyer