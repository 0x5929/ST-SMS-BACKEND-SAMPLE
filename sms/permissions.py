from rest_framework import permissions

# add custom permissions for the Student Management System
# all users are able to GET
# only super users can POST, PUT, PATCH, DELETE
# there should really be only one superuser in one school
# to prevent data coming in from multiple directions, its more safe to have other staff to paper record it, and then superuser enters data
