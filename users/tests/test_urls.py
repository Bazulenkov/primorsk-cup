from django.contrib.auth import get_user_model
from django.test import Client, TestCase

User = get_user_model()


# class GroupURLTests(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.user = User.objects.create(
#             email="test@fake.ru", password="1qazXSW@"
#         )

#     def setUp(self):
#         # Создаем неавторизованный клиент
#         self.guest_client = Client()

#         # Создаем пользователя
#         # self.user = User.objects.create(username="Pupkin")

#         # Создаем второй клиент
#         # self.authorized_client = Client()
#         # Авторизуем пользователя
#         # self.authorized_client.force_login(self.user)

#     # Шаблоны по адресам
#     def test_urls_uses_correct_template(self):
#         """URL-адрес использует соответствующий шаблон."""
#         templates_url_names = {
#             "index.html": "/",
#             "group.html": "/group/test-slug/",
#             "new.html": "/new/",
#         }
#         for template, reverse_name in templates_url_names.items():
#             with self.subTest():
#                 response = self.authorized_client.get(reverse_name)
#                 self.assertTemplateUsed(response, template)

#     # Проверяем редиректы для неавторизованного пользователя
#     def test_new_post_url_redirect_anonymous_on_admin_login(self):
#         """Страница по адресу /new/ перенаправит анонимного
#         пользователя на страницу логина.
#         """
#         response = self.guest_client.get("/new/", follow=True)
#         self.assertRedirects(response, ("/auth/login/?next=%2Fnew%2F"))

#     def test_current_group_url_redirect_anonymous_on_admin_login(self):
#         """Страница по адресу /group/test-slug/ перенаправит анонимного
#         пользователя на страницу логина.
#         """
#         response = self.guest_client.get("/group/test-slug/", follow=True)
#         self.assertRedirects(
#             response, ("/auth/login/?next=%2Fgroup%2Ftest-slug%2F")
#         )

#     def test_home_url_exists_at_desired_location(self):
#         """Главная страница / доступна любому пользователю."""
#         response = self.guest_client.get("/")
#         self.assertEqual(response.status_code, 200)

#     def test_create_post_url_exists_at_desired_location_authorized(self):
#         """Страница /new/ доступна авторизованному
#         пользователю."""
#         response = self.authorized_client.get("/new/")
#         self.assertEqual(response.status_code, 200)

#     def test_group_slug_url_exists_at_desired_location_authorized(self):
#         """Страница /group/test-slug/ доступна авторизованному
#         пользователю."""
#         response = self.authorized_client.get("/group/test-slug/")
#         self.assertEqual(response.status_code, 200)


class StaticURLTests(TestCase):
    def setUp(self):
        # Устанавливаем данные для тестирования
        # Создаём экземпляр клиента. Он неавторизован.
        self.guest_client = Client()

    def test_homepage(self):
        # Отправляем запрос через client,
        # созданный в setUp()
        response = self.guest_client.get("/")
        self.assertEqual(response.status_code, 200)
