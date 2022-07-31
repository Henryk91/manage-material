from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
)


class UserView(CreateAPIView, RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def patch(self, request, *args, **kwargs):
        response = super().patch(request)
        return response
