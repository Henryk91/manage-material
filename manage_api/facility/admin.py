from django.contrib import admin
from .models import Facility, DeliveryItem


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    pass


@admin.register(DeliveryItem)
class DeliveryItemAdmin(admin.ModelAdmin):
    pass
