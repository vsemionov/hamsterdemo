from django.conf.urls import url, include
from rest_framework import routers

from .views import NotebookViewSet, NoteViewSet, ErrorViewSet


router = routers.DefaultRouter()
router.register(r'notebooks', NotebookViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'error', ErrorViewSet, base_name='error')

urlpatterns = [
    url(r'^', include(router.urls)),
]
