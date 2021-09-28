from rest_framework import permissions

# add custom permissions for the Student Management System
# all authenticated users are able to GET all models, and all other actions on Student
# only staff users can POST, PUT, PATCH, DELETE rotation, program and school
# there should really be only one staff in one school, and maybe a few regular users. In all schools, one superuser, one main database
# to prevent data coming in from multiple directions, its more safe to have other user to paper record it, and then staff enters data


class IsAuthenticatedToReadOnly(permissions.BasePermission):
    message = 'Sorry, you must be at least authenticated to perform this action.'

    def has_permission(self, request, view):
        return True if request.method in permissions.permissions.SAFE_METHODS and request.user.is_authenticated else False

    def has_object_permission(self, request, view, obj):
        return True if request.method in permissions.permissions.SAFE_METHODS and request.user.is_authenticated else False


class IsSuperuser(permissions.BasePermission):
    message = 'Sorry, you must be a superuser to perform this action.'

    def has_permission(self, request, view):
        return True if request.user.is_superuser else False

    def has_object_permission(self, request, view, obj):
        return True if request.user.is_superuser else False
