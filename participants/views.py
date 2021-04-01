import weasyprint
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView

from users.forms import UpdateForm
from users.models import Discipline

from .mixins import UserProfileTestMixin

User = get_user_model()


class ParticipantListView(LoginRequiredMixin, ListView):
    """Главная страница.

    Просмотр списка участников."""

    model = User
    template_name = "participants.html"
    context_object_name = "participant_list"

    def __init__(self, **kwargs) -> None:
        self.all_disciplines = Discipline.objects.all()
        super().__init__(**kwargs)


class ParticipantView(LoginRequiredMixin, DetailView):
    """Просмотр деталей участника."""

    model = User
    template_name = "user_details.html"
    context_object_name = "participant"


class ParticipantUpdate(LoginRequiredMixin, UserProfileTestMixin, UpdateView):
    """Редактирование данных участниа."""

    form_class = UpdateForm
    model = User
    template_name = "signup.html"
    context_object_name = "participant"


class ParticipantDelete(LoginRequiredMixin, UserProfileTestMixin, DeleteView):
    """Удаление участника соревнований (и пользователя сайта)."""

    model = User
    template_name = "user_confirm_delete.html"
    success_url = reverse_lazy("index")


def list_pdf(request):
    """Вывод списка участников в pdf."""
    participant_list = User.objects.all()
    disciplines = Discipline.objects.all()

    html = render_to_string(
        "participantlist_pdf.html",
        {"participant_list": participant_list, "disciplines": disciplines},
    )
    response = HttpResponse(content_type="application/pdf; charset=utf-8")
    response["Content-Disposition"] = 'filename="list.pdf"'
    weasyprint.HTML(string=html).write_pdf(
        response,
        stylesheets=[
            weasyprint.CSS(str(settings.STATIC_ROOT) + "/list_pdf.css")
        ],
    )
    return response
