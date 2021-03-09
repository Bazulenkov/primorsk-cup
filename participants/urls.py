from django.urls import path

from . import views

urlpatterns = [
    path("participantlist/", views.list_pdf, name="participants_list_pdf"),
    path(
        "<int:pk>/",
        views.ParticipantView.as_view(),
        name="participant-details",
    ),
    path(
        "<int:pk>/update/",
        views.ParticipantUpdate.as_view(),
        name="participant_update",
    ),
    path(
        "<slug:discipline>/",
        views.ParticipantListView.as_view(),
        name="discipline_participants",
    ),
    path("", views.ParticipantListView.as_view(), name="participants"),
]
