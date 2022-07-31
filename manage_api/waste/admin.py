from django.contrib import admin
from .models import MaterialType, WasteType, WasteCategory


@admin.register(MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(WasteType)
class WasteTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(WasteCategory)
class WasteCategoryAdmin(admin.ModelAdmin):
    pass
