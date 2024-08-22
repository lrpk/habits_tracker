from django.urls import path

from . import views

urlpatterns = [
    path("", views.habits_view, name="habits_view")
]
