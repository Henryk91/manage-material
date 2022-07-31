from django.urls import path

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

from .views import FacilityView, DeliveryItemView, FacilityWasteQuantityViewSet, TotalWasteQuantityViewSet

router.register("facility", FacilityView, "facility")
app_urls = [
    path("delivery/", DeliveryItemView.as_view(), name="delivery"),
    path("facility-quantity/<str:facility_id>/", FacilityWasteQuantityViewSet.as_view(), name="facility-quantity"),
    path("total-quantity/", TotalWasteQuantityViewSet.as_view(), name="total-quantity"),
]
app_name = 'facility'
urlpatterns = app_urls + router.urls
