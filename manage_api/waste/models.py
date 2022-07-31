from django.db import models


class MaterialType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WasteType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WasteCategory(models.Model):
    waste_type = models.ForeignKey(
        WasteType, related_name="category_waste", on_delete=models.PROTECT
    )
    material_type = models.ForeignKey(
        MaterialType, related_name="category_material", on_delete=models.PROTECT
    )

    @property
    def name(self):
        return f"{self.waste_type.name}-{self.material_type.name}"

    def __str__(self):
        return self.name
