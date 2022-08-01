from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from manage_api.waste.models import WasteCategory, WasteType, MaterialType


from .models import DeliveryItem, Facility


class FacilitySerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if "name" not in attrs:
            raise ValidationError({"detail": "Facility Needs a name"})
        return attrs

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = Facility
        fields = "__all__"


class DeliveryItemSerializer(serializers.Serializer):
    facility = serializers.IntegerField()
    weight = serializers.IntegerField()
    material_type = serializers.IntegerField()
    waste_type = serializers.IntegerField()

    def validate(self, attrs):
        facility = Facility.objects.filter(id=str(attrs["facility"]))
        if facility.count() == 0:
            raise ValidationError({"detail": "Facility id not found"})
        waste_type = WasteType.objects.filter(id=attrs["waste_type"])
        if waste_type.count() == 0:
            raise ValidationError({"detail": "Waste Type id not found"})
        material_type = MaterialType.objects.filter(id=attrs["material_type"])
        if material_type.count() == 0:
            raise ValidationError({"detail": "Material Type id not found"})
        if attrs["weight"] < 0:
            raise ValidationError({"detail": "Weight cannot be less than zero"})
        return {
            "material_type": material_type.first(),
            "waste_type": waste_type.first(),
            "facility": facility.first(),
            "weight": attrs["weight"],
        }

    def create(self, validated_data):
        waste_category, created = WasteCategory.objects.get_or_create(
            waste_type=validated_data["waste_type"],
            material_type=validated_data["material_type"],
        )

        return DeliveryItem.objects.create(
            waste_category=waste_category,
            facility=validated_data["facility"],
            weight=validated_data["weight"],
            user=self.context["request"].user
        )

    class Meta:

        fields = ("facility", "weight", "material_type", "waste_type")


class WasteCatagoryQuantitySerializer(serializers.Serializer):
    category_id = serializers.CharField()
    category_name = serializers.CharField()
    waste_type = serializers.CharField()
    material_type = serializers.CharField()
    weight = serializers.CharField()

    class Meta:
        ref_name = "WasteCatagoryQuantity"


class FacilityWasteQuantitySerializer(serializers.Serializer):
    facility_id = serializers.CharField(required=False)
    facility_name = serializers.CharField(required=False)
    catagory_list = WasteCatagoryQuantitySerializer(many=True, required=False)

    def validate(self, attr):
        facility = Facility.objects.filter(id=attr["facility_id"])
        if facility.count() == 0:
            raise ValidationError({"detail": "Facility id not found"})

        return attr

    class Meta:
        ref_name = "FacilityWasteQuantity"


class TotalWasteQuantitySerializer(serializers.Serializer):
    catagory_list = WasteCatagoryQuantitySerializer(many=True, required=False)

    class Meta:
        ref_name = "TotalWasteQuantity"
