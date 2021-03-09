from django import forms
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from posts.models import Group, Post

User = get_user_model()


class PostPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Создадим запись в БД
        cls.user = User.objects.create(username="testuser")

        cls.group = Group.objects.create(
            title="Test",
            description="Группа тест",
            slug="slugtest",
        )

        cls.group_without_post = Group.objects.create(
            title="GroupTest2",
            description="2 Группа тест",
            slug="slugtest2",
        )

        cls.post = Post.objects.create(
            text="Заголовок тестового поста",
            group=cls.group,
            author=cls.user,
        )

    def setUp(self):
        # Создаем авторизованный клиент
        self.user = User.objects.create(username="Pupkin")
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    # Проверяем используемые шаблоны
    def test_pages_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        # Собираем в словарь пары "имя_html_шаблона: name"
        templates_pages_names = {
            "index.html": reverse("posts:index"),
            "new.html": reverse("posts:new_post"),
            "group.html": (reverse("posts:group", kwargs={"slug": "slugtest"})),
        }
        # Проверяем, что при обращении к name вызывается
        # соответствующий HTML-шаблон
        for template, reverse_name in templates_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.authorized_client.get(reverse_name)
                self.assertTemplateUsed(response, template)

    # Проверка словаря контекста главной страницы (в нём передаётся форма)
    def test_home_page_show_correct_context(self):
        """Шаблон home сформирован с правильным контекстом."""
        response = self.authorized_client.get(reverse("posts:index"))

        # Взяли первый элемент из списка и проверили, что его содержание
        # совпадает с ожидаемым
        post_text_0 = response.context.get("posts")[0]
        self.assertEqual(post_text_0, self.post)

    # Проверка словаря контекста страницы групп
    def test_group_page_show_correct_context(self):
        """Шаблон group сформирован с правильным контекстом."""
        response = self.authorized_client.get(
            reverse("posts:group", kwargs={"slug": self.group.slug})
        )

        # Взяли первый элемент из списка и проверили, что его содержание
        # совпадает с ожидаемым
        group_context_1 = response.context.get("group").slug
        self.assertEqual(group_context_1, "slugtest")
        group_context_2 = response.context.get("posts")[0]
        self.assertEqual(group_context_2, self.post)

    # Проверка словаря контекста страницы групп(не содержит пост)
    def test_group_page_dont_show_context_from_other_group(self):
        """Шаблон group сформирован без поста в группе."""
        response = self.authorized_client.get(
            reverse("posts:group", kwargs={"slug": self.group_without_post.slug})
        )

        # Взяли первый элемент из списка и проверили, что его содержание
        # совпадает с ожидаемым
        group1_context_0 = response.context["posts"]
        self.assertNotIn(self.post, group1_context_0)

    # Проверка словаря контекста страницы нового поста
    def test_new_post_show_correct_context(self):
        """Шаблон group сформирован с правильным контекстом."""
        response = self.authorized_client.get(reverse("posts:new_post"))

        # Список ожидаемых типов полей формы:
        # указываем, объектами какого класса должны быть поля формы
        form_fields = {
            "text": forms.fields.CharField,
            "group": forms.fields.ChoiceField,
        }

        # Проверяем, что типы полей формы в словаре context
        # соответствуют ожиданиям
        for value, expected in form_fields.items():
            with self.subTest(value=value):
                form_field = response.context.get("form").fields.get(value)
                # Проверяет, что поле формы является экземпляром
                # указанного класса
                self.assertIsInstance(form_field, expected)
