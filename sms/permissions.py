from rest_framework import permissions

# ONLY is_office = True users can access, then the following:
# SUPERUSERS: can do everything
# STAFF: can only do everything in Rotation and Student
# OTHERS: can only view everything


class IsAuthenticatedOfficeUserToReadOnly(permissions.BasePermission):
    message = 'Sorry, you must be at least authenticated and an office user to perform this action.'

    def has_permission(self, request, view):
        return True if request.user.is_authenticated and request.user.is_office and request.method in permissions.SAFE_METHODS else False


class IsAuthenticatedOfficeAdmin(permissions.BasePermission):
    message = 'Sorry, you must be an office administrator to perform this action.'

    def has_permission(self, request, view):
        return True if request.user.is_authenticated and request.user.is_staff and request.user.is_office else False


class IsSuperuser(permissions.BasePermission):
    message = 'Sorry, you must be a superuser to perform this action.'

    def has_permission(self, request, view):
        return True if request.user.is_superuser else False
