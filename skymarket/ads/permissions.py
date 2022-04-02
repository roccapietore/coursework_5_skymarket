from rest_framework.permissions import BasePermission
from users.managers import UserRole


class IsUser(BasePermission):
    message = "This function is only available for users"

    def has_permission(self, request, view):
        return bool(request.user.role == UserRole.USER and request.user.is_user)


class IsOwnerPermission(BasePermission):
    message = 'This function is only available for ad`s owner'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

