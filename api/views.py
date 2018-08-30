from rest_framework import viewsets, mixins

from .models import Notebook, Note
from .serializers import NotebookSerializer, NoteSerializer
from .error import HamsterException


class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class ErrorViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    view_name = 'Error'

    def get_view_name(self):
        return self.view_name

    def list(self, request, *args, **kwargs):
        raise HamsterException(555, 'custom_error')
