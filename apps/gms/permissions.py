from rest_framework import permissions

# from core.settings.constants import PROGRAM_NAMES

from django.conf import settings

PROGRAM_NAMES = getattr(settings, 'PROGRAM_NAMES')

# ONLY is_istructor = True users can access, then do the following:
# SUPERUSERS: can do everything
# ADMIN: can do everything within school and all courses
# STAFF: can do everything within school and limited to assigned courses
# REG USER: can do everything within school, email and limited to assigned courses as well


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


class IsAuthenticatedAdminInstructor(permissions.BasePermission):
    message = 'Please be sure to log in with an admin instructor account and try again.'

    def has_permission(self, request, view):
        if request.user.is_authenticated and \
           request.user.is_instructor and \
           request.user.is_admin:

            return True
        else:
            return False


class IsAuthenticatedCNAStaffInstructor(permissions.BasePermission):
    message = 'Please be sure to log in with a CNA staff instructor account and try again'

    def get_cna_program_name(self):
        for program in PROGRAM_NAMES:
            if 'CNA' in program:
                return 'CNA'

    def has_permission(self, request, view):
        if request.user.is_authenticated and \
           request.user.is_instructor and \
           request.user.is_staff and\
           self.get_cna_program_name() == 'CNA':
            return True
        else:
            return False


class IsAuthenticatedHHAStaffInstructor(permissions.BasePermission):
    message = 'Please be sure to log in with a HHA staff instructor account and try again'

    def get_hha_program_name(self):
        for program in PROGRAM_NAMES:
            if 'HHA' in program:
                return 'HHA'

    def has_permission(self, request, view):
        if request.user.is_authenticated and \
           request.user.is_instructor and \
           request.user.is_staff and\
           self.get_hha_program_name() == 'HHA':
            return True
        else:
            return False
