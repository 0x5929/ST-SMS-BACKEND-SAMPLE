from rest_framework import permissions, SAFE_METHODS

# add custom permissions for the Student Management System
# all users are able to GET
# only super users can POST, PUT, PATCH, DELETE
# there should really be only one superuser in one school
# to prevent data coming in from multiple directions, its more safe to have other staff to paper record it, and then superuser enters data


class IsSuperuserOrAuthenticatedReadOnly(permissions.BasePermission):
    message = 'Sorry, you do not have sufficient permissions to do such actions.'

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True

        if request.user.is_authenticated and not request.user.is_superuser:
            return request.method in SAFE_METHODS

        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.is_superuser:
            return True

        if request.user.is_authenticated and not request.user.is_superuser:
            return request.method in SAFE_METHODS

        return False
