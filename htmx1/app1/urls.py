from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.test, name="test"),
    path("test_post/<int:a>/<str:b>/", views.test_post, name="test_post"),
    path("bulk_update/",views.bulk_update, name="bulk_update"),
    path("app1/partials/activate/",views.activate, name="activate"),
    path("app1/partials/deactivate/",views.deactivate, name="deactivate"),
    # path("app1/partials/languages/",views.languages, name="languages"),
    # path("contact/<int:id>/",views.contact,name="contact"),
    # path("contact/<int:id>/edit/",views.contact_form,name="contact_form"),
    path("contact/<int:id>/",views.ContactView.as_view(),name="contact")
]
