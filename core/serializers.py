from rest_framework import serializers


class UserViewSetInputSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(min_value=1)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
