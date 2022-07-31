from .services import WasteQuantityService
from .serializers import (
    FacilitySerializer,
    DeliveryItemSerializer,
    FacilityWasteQuantitySerializer,
    TotalWasteQuantitySerializer,
)
from .models import Facility, DeliveryItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
)
from rest_framework import status
from .permissions import FacilityUser


class FacilityView(ModelViewSet):
    serializer_class = FacilitySerializer
    permission_classes = (IsAuthenticated, FacilityUser)

    def get_queryset(self):
        return Facility.objects.all()


class DeliveryItemView(CreateAPIView):
    serializer_class = DeliveryItemSerializer
    permission_classes = (IsAuthenticated, FacilityUser)

    def get_queryset(self):
        return DeliveryItem.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        return Response(request.data, status=status.HTTP_201_CREATED)


class FacilityWasteQuantityViewSet(RetrieveAPIView):
    serializer_class = FacilityWasteQuantitySerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, facility_id=None):
        serializer = FacilityWasteQuantitySerializer(data={"facility_id": facility_id})
        serializer.is_valid(raise_exception=True)

        service = WasteQuantityService()

        return Response(
            service.get_waste_quantity_by_facility(facility_id),
            status=status.HTTP_200_OK,
        )


class TotalWasteQuantityViewSet(RetrieveAPIView):
    serializer_class = TotalWasteQuantitySerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        service = WasteQuantityService()

        return Response(
            service.get_total_waste_quantity(),
            status=status.HTTP_200_OK,
        )
