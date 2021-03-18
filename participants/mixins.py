from django.contrib.auth.mixins import UserPassesTestMixin


class UserProfileTestMixin(UserPassesTestMixin):
    """ Проверяем свой ли профиль пытается редактировать/удалить User."""

    def test_func(self):
        return self.request.user.id == self.kwargs.get("pk")
