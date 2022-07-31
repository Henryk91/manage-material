from rest_framework.permissions import BasePermission


class FacilityUser(BasePermission):
    message = "Not facility user"

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.user in obj.users.all()
