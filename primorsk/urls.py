"""primorsk URL Configuration."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("adminka/", admin.site.urls),
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("about/", include("about.urls", namespace="about")),
    path("", include("participants.urls")),
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
