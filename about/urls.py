from django.urls import path
from django.views.generic import TemplateView

app_name = "about"

urlpatterns = [
    path(
        "author/",
        TemplateView.as_view(template_name="author.html"),
        name="author",
    ),
    path(
        "tech/",
        TemplateView.as_view(template_name="tech.html"),
        name="tech",
    ),
    path(
        "competitions/",
        TemplateView.as_view(template_name="competitions.html"),
        name="competitions",
    ),
    path(
        "contacts",
        TemplateView.as_view(template_name="contacts.html"),
        name="contacts",
    ),
    path(
        "sponsors",
        TemplateView.as_view(template_name="sponsors.html"),
        name="sponsors",
    )
]
