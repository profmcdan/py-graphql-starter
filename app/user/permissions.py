from rest_framework import permissions
from django_graphene_permissions.permissions import BasePermission


class IsAuthenticated(BasePermission):
    """Allows access only to admin users. """
    message = "You have to be logged in to perform this action"

    @staticmethod
    def has_permission(context):
        return context.user and context.user.is_authenticated


class IsSuperAdmin(permissions.BasePermission):
    """Allows access only to super admin users. """
    message = "Only Super Admins are authorized to perform this action."

    def has_permission(self, request, view):
        return bool(request.user and request.user.roles and 'SUPERADMIN' in request.user.roles)


class IsAdmin(permissions.BasePermission):
    """Allows access only to admin users. """
    message = "Only Admins are authorized to perform this action."

    def has_permission(self, request, view):
        return bool(request.user and request.user.roles and 'ADMIN' in request.user.roles)


class IsBasicUser(permissions.BasePermission):
    """Allows access only to talent users. """
    message = "Only Basic users are authorized to perform this action."

    def has_permission(self, request, view):
        return bool(request.user and request.user.roles and 'BASIC' in request.user.roles)
