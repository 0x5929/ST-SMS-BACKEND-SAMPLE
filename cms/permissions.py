from rest_framework import permissions

# ONLY is_recruit = True users can access, then do the following:
# SUPERUSERS: can do everything
# STAFF: can do everything but limited by ownership/obj assignment, and school
# OTHERS: same as STAFF

# NOTE: limits or limitations mean queryset will limit each user (excluding superusers)
# to do actions on their own school's and their own client's objects (assigned to sales/recruit staff by emails).
# superusers can do all

#  NOTE: so in this app, is_staff and regular user have no difference in permissions, all can only see their own school's own client's (unless added to recruit_emails)


class IsSuperuser(permissions.BasePermission):
    message = 'Sorry, you must be a superuser to perform this action.'

    def has_permission(self, request, view):
        return True if request.user.is_authenticated and request.user.is_superuser else False
