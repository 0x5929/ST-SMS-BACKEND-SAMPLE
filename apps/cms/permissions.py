from rest_framework import permissions


class IsSuperuser(permissions.BasePermission):
    message = 'Sorry, you must be a superuser to perform this action.'

    def has_permission(self, request, view):
        return True if request.user.is_authenticated and request.user.is_superuser else False


class IsAuthenticatedAndRecruit(permissions.BasePermission):
    message = 'Please be sure to log in with a recruit account and try again.'

    def has_permission(self, request, view):

        return True if request.user.is_authenticated and request.user.is_recruit else False
