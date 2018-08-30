from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('require_auth', views.require_auth),
]
