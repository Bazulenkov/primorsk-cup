from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

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
            "first_name",
            "last_name",
            "email",
            "discipline",
            "trainer",
            "club",
            "city",
            "birthday",
            "category",
            "image",
        )


class UpdateForm(UserCreationForm):
    """Cобственный класс для формы регистрации."""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "discipline",
            "trainer",
            "club",
            "city",
            "birthday",
            "category",
            "image",
        )
