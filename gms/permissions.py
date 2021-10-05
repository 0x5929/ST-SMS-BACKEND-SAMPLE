from rest_framework import permissions

from core.settings.constants import PROGRAM_NAMES

# ONLY is_istructor = True users can access, then do the following:
# SUPERUSERS: can do everything
# STAFF: no one will be assigned as staff, as there
# OTHERS: same as STAFF


class IsSuperuser(permissions.BasePermission):
    message = 'Sorry, you must be a superuser to perform this action.'

    def has_permission(self, request, view):
        return True if request.user.is_authenticated and request.user.is_superuser else False


class IsAuthenticatedCNAInstructor(permissions.BasePermission):
    message = 'Please be sure to log in with a CNA intructor account and try again.'

    def get_cna_program_name(self):
        for program in PROGRAM_NAMES:
            if 'CNA' in program:
                return 'CNA'

    def has_permission(self, request, view):
        program_name = self.get_cna_program_name()

        if program_name:
            if request.user.is_authenticated and \
                    request.user.is_instructor and \
                    program_name in request.user.programs:
                return True

        return False


class IsAuthenticatedHHAInstructor(permissions.BasePermission):
    message = 'Please be sure to log in with a CNA intructor account and try again.'

    def get_hha_program_name(self):
        for program in PROGRAM_NAMES:
            if 'HHA' in program:
                return 'HHA'

    def has_permission(self, request, view):
        program_name = self.get_hha_program_name()

        if program_name:
            if request.user.is_authenticated and \
                    request.user.is_instructor and \
                    program_name in request.user.programs:
                return True

        return False
