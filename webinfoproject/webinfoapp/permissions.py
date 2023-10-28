
from rest_framework import permissions

class AdminPlatformPermission(permissions.BasePermission):
    message = "You do not have permission to perform this action on platforms."
    def has_permission(self, request, view):
        return (
            request.user.has_perm('webinfoapp.add_platform_model') and
            request.user.has_perm('webinfoapp.change_platform_model') and
            request.user.has_perm('webinfoapp.delete_platform_model')
        )

class TechnicianPlatformPermission(permissions.BasePermission):
    message = "You do not have permission to edit platforms."
    def has_permission(self, request, view):
        return request.user.has_perm('webinfoapp.change_platform_model')

class AdminProductPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.has_perm('webinfoapp.add_product_model') and
            request.user.has_perm('webinfoapp.change_product_model') and
            request.user.has_perm('webinfoapp.delete_product_model')
        )

class TechnicianProductPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('webinfoapp.change_product_model')

class AdminDevicePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.has_perm('webinfoapp.add_device_model') and
            request.user.has_perm('webinfoapp.change_device_model') and
            request.user.has_perm('webinfoapp.delete_device_model')
        )

class TechnicianDevicePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('webinfoapp.change_device_model')
