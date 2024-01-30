from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.test, name="test"),
    path("test_put/<int:id>/", views.test_put, name="test_put"),
]
