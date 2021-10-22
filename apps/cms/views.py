from rest_framework import viewsets, response
from django_filters import rest_framework as filters

from .models import Client, Note
from .permissions import IsSuperuser, IsAuthenticatedAndRecruit
from .serializers import ClientSerializer, NoteSerializer
from .filters import CMSClientFilter, CMSNoteFilter
from .utils import FilterHandler

class ClientView(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsSuperuser | IsAuthenticatedAndRecruit]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CMSClientFilter

    def get_queryset(self):
        return Client.objects.get_query(self.request)

    # to ensure query parameters are done correctly
    def list(self, request, *args, **kwargs):
        if not FilterHandler.is_valid_query_params(request.query_params, CMSClientFilter.Meta.fields):
            return response.Response([])
        return super(ClientView, self).list(request, *args, **kwargs)


class NoteView(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsSuperuser | IsAuthenticatedAndRecruit]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CMSNoteFilter

    def get_queryset(self):
        return Note.objects.get_query(self.request)

    # to ensure query parameters are done correctly
    def list(self, request, *args, **kwargs):
        if not FilterHandler.is_valid_query_params(request.query_params, CMSNoteFilter.Meta.fields):
            return response.Response([])
        return super(NoteView, self).list(request, *args, **kwargs)
