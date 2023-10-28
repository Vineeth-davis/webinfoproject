from rest_framework.permissions import BasePermission

class IsAdministrator(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.is_administrator

class IsTechnician(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.is_technician

class CanEditPlatform(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method in ('PUT', 'PATCH'):
            return request.user.has_perm('app.edit_platform')
        return True

class CanEditProduct(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method in ('PUT', 'PATCH'):
            return request.user.has_perm('app.edit_product')
        return True

class CanEditDevice(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method in ('PUT', 'PATCH'):
            return request.user.has_perm('app.edit_device')
        return True