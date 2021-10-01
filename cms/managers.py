import uuid

from django.db import models


class ClientManager(models.Manager):

    # limit by school, then limit by ownership, except for superuser
    def get_query(self, request):
        if request.user.is_superuser:
            return super(NoteManager, self).get_queryset.all()

        return super(ClientManager, self).get_queryset.filter(
            school_name__exact=request.user.school_name).filter(
                recruit_emails__overlap=[request.user.email])


class NoteManager(models.Manager):

    # limit by school, then limit by ownership, except for superuser
    def get_query(self, request):
        if request.user.is_superuser:
            return super(NoteManager, self).get_queryset.all()

        return super(NoteManager, self).get_queryset.filter(
            client__school_name__exact=request.user.school_name).filter(
                client__recruit_emails__overlap=[request.user.email])

    def create_or_update_note(self, validated_data, instance=None):
        # get client ID from request
        client_id = uuid.UUID(str(validated_data.get('client')))

        # retrieve client from DB
        from .models import Client
        client = Client.objects.get(client_uuid__exact=client_id)

        # add client to note object
        validated_data['client'] = client

        return (instance, validated_data) if instance else validated_data
