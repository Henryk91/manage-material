from manage_api.waste.services import WasteCategoryHistoryService
from .serializers import (
    WasteCategorySerializer,
    MaterialTypeSerializer,
    WasteTypeSerializer,
    WasteCategoryHistorySerializer,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import WasteCategory, MaterialType, WasteType


class WasteCategoryView(ModelViewSet):
    serializer_class = WasteCategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return WasteCategory.objects.all()


class WasteTypeView(ModelViewSet):
    serializer_class = WasteTypeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return WasteType.objects.all()


class MaterialTypeView(ModelViewSet):
    serializer_class = MaterialTypeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MaterialType.objects.all()


class WasteCategoryHistoryViewSet(RetrieveAPIView):
    serializer_class = WasteCategoryHistorySerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, category_id=None):
        serializer = WasteCategoryHistorySerializer(data={"category_id": category_id})
        serializer.is_valid(raise_exception=True)

        service = WasteCategoryHistoryService()

        return Response(
            service.get_waste_history_by_category(category_id),
            status=status.HTTP_200_OK,
        )
