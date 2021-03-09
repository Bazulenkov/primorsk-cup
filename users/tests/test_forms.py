from django.test import Client, TestCase
from django.urls import reverse
from posts.forms import PostForm
from posts.models import Group, Post, User


class TaskCreateFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Создаем форму, если нужна проверка атрибутов
        cls.form = PostForm()

    def setUp(self):
        # Создаем неавторизованный клиент
        self.guest_client = Client()

        # Создаем авторизованный клиент
        self.user = User.objects.create(username="Pupkin")
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

        self.group = Group.objects.create(
            title="Test",
            description="Группа тест",
            slug="slugtest",
        )

        # Создаем запись в базе данных для проверки существует ли она
        Post.objects.create(
            text="Тестовый текст",
            group=self.group,
            author=self.user,
        )

    def test_create_post(self):
        """Валидная форма создает новый пост"""
        # Получим первый тестовый пост и если он есть удалеим его
        existing_post = Post.objects.first()
        existing_post.delete()
        existing_post.save()

        # Подсчитаем количество постов, должно быть 0
        posts_count = Post.objects.count()

        # Создаем группу для передачи ее id в форму
        group_for_create = Group.objects.create(
            title="test title post 2",
            slug="test_slug_post_2",
            description="test description post 2",
        )

        # Создаем тестовые данные формы
        form_data = {
            "text": "Тестовый текст",
            "group": group_for_create.id,
            "author": self.user,
        }
        # Отправляем POST-запрос
        res = self.authorized_client.post(
            reverse("posts:new_post"), data=form_data, follow=True
        )

        # у нас app_name = 'posts' и я хочу получить первый пост на главной
        created_post = res.context["posts"][0]
        # Проверяем, сработал ли редирект
        self.assertRedirects(res, "/")
        # Проверяем, увеличилось ли число постов
        self.assertEqual(Post.objects.count(), posts_count + 1)
        # Проверим что текст поста совпадает с переданным из формы
        self.assertEqual(created_post.text, form_data["text"])
        # Проверим что группа совпадает совпадает с переданной из формы
        self.assertEqual(created_post.group, group_for_create)
        # Проверим что автор совпадает совпадает с автором из формы
        self.assertEqual(created_post.author, self.user)
