from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

User = get_user_model()


class CreationForm(UserCreationForm):
    """Cобственный класс для формы регистрации."""

    def __init__(self, *args, **kwargs):
        super(CreationForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["birthday"].widget = AdminDateWidget()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "sailnum",
            "discipline",
            "trainer",
            "club",
            "city",
            "birthday",
            "category",
            "image",
        )


# Сделал отдельную форму для редактирования, чтобы при редактировании не
# вылезало полей изменения пароля. Под изменения пароля использую штатную форму
# Django
class UpdateForm(ModelForm):
    """Cобственный класс для формы редактирования профиля (регистрации)."""

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["birthday"].widget = AdminDateWidget()

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "sailnum",
            "discipline",
            "trainer",
            "club",
            "city",
            "birthday",
            "category",
            "image",
        )
