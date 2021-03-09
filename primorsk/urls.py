"""primorsk URL Configuration."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView

urlpatterns = [
    path("adminka/", admin.site.urls),
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("about/", include("about.urls", namespace="about")),
    path("participants/", include("participants.urls")),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
]

handler404 = "primorsk.views.page_not_found"  # noqa
handler500 = "primorsk.views.server_error"  # noqa

if settings.DEBUG:
    # for debug media
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
