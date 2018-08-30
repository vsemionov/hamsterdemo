from django.conf.urls import url, include
from rest_framework import routers

from .views import NotebookViewSet, NoteViewSet


router = routers.DefaultRouter()
router.register(r'notebooks', NotebookViewSet)
router.register(r'notes', NoteViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
