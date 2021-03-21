from django.test import TestCase
from posts.models import Group, Post, User


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Создаём тестовую запись в БД
        cls.user = User.objects.create(username="testuser")

        cls.group = Group.objects.create(
            title="Test",
            description="Группа тест",
            slug="slugtest",
        )

        cls.post = Post.objects.create(
            text="Заголовок тестового поста",
            group=cls.group,
            author=cls.user,
        )

    def test_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        post = PostModelTest.post
        field_verboses = {
            "text": "Текст",
            "group": "Группа",
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    post._meta.get_field(value).verbose_name, expected
                )

    def test_help_text(self):
        """help_text в полях совпадает с ожидаемым."""
        post = PostModelTest.post
        field_help_texts = {
            "text": "Введите текст вашего сообщения",
            "group": "Укажите группу для публикации",
        }
        for value, expected in field_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    post._meta.get_field(value).help_text, expected
                )

    def test_object_name_is_title_field(self):
        """__str__  post - это строчка с содержимым post.title."""
        post = PostModelTest.post
        expected_object_name = f"{post.text[:15]}"
        self.assertEquals(expected_object_name, str(post))

        group = PostModelTest.group
        expected_object_name = group.title
        self.assertEquals(expected_object_name, str(group))
