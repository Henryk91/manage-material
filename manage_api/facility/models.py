from django.db import models
from manage_api.user.models import User
from model_utils.models import TimeStampedModel
from manage_api.waste.models import WasteCategory


class Facility(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    users = models.ManyToManyField(User, related_name="users", blank=True)

    def __str__(self):
        return self.name


class DeliveryItem(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    facility = models.ForeignKey(
        Facility, related_name="delivery", on_delete=models.PROTECT
    )
    waste_category = models.ForeignKey(
        WasteCategory, related_name="delivery_waste_category", on_delete=models.PROTECT
    )
    user = models.ForeignKey(
        User, related_name="delivery_items", on_delete=models.PROTECT
    )

    weight = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Delivery {self.id} ({self.facility}) {self.weight} kg"
