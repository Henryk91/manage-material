from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import WasteCategory, MaterialType, WasteType


class WasteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteCategory
        fields = "__all__"


class MaterialTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialType
        fields = "__all__"


class WasteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteType
        fields = "__all__"


class WasteCategoryHistoryItemSerializer(serializers.Serializer):
    quantity = serializers.CharField()
    time = serializers.CharField()
    username = serializers.CharField()

    class Meta:
        ref_name = "WasteCatagoryHistoryItem"


class WasteCategoryHistorySerializer(serializers.Serializer):
    category_id = serializers.CharField(required=False)
    catagory_list = WasteCategoryHistoryItemSerializer(many=True, required=False)

    def validate(self, attr):
        facility = WasteCategory.objects.filter(id=attr["category_id"])
        if facility.count() == 0:
            raise ValidationError({"detail": "Category id not found"})

        return attr

    class Meta:
        ref_name = "WasteCategoryHistory"
