from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


class UserSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if self.name not in None:
            raise ValidationError({"detail": "User Needs a name"})

        return attrs

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = User
        fields = "__all__"
