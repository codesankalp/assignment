from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS, BasePermission


class BoxPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff and request.user.is_authenticated
