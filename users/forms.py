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


class UpdateForm(ModelForm):
    """Cобственный класс для формы редактирования профиля (регистрации)."""

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
