from django.urls import path

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from .views import (
    WasteCategoryView,
    WasteTypeView,
    MaterialTypeView,
    WasteCategoryHistoryViewSet,
)

router.register("waste-category", WasteCategoryView, "waste-category")
router.register("waste-type", WasteTypeView, "waste-type")
router.register("material-type", MaterialTypeView, "material-type")

app_urls = [
    path(
        "category-history/<str:category_id>/",
        WasteCategoryHistoryViewSet.as_view(),
        name="category-history",
    ),
]

app_name = "waste"
urlpatterns = app_urls + router.urls
