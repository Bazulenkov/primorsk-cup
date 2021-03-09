# Generated by Django 3.1.6 on 2021-02-16 13:38

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discipline",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=10)),
                ("slug", models.SlugField(max_length=10, unique=True)),
                ("color", models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email address"
                    ),
                ),
                (
                    "trainer",
                    models.CharField(blank=True, max_length=50, verbose_name="Тренер"),
                ),
                (
                    "club",
                    models.CharField(blank=True, max_length=50, verbose_name="Клуб"),
                ),
                ("city", models.CharField(max_length=50, verbose_name="Город")),
                ("birthday", models.DateField(null=True, verbose_name="Дата рождения")),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        choices=[
                            (None, "-"),
                            ("1", "1й разряд"),
                            ("2", "2й разряд"),
                            ("3", "3й разряд"),
                            ("КМС", "КМС"),
                            ("МС", "МС"),
                        ],
                        max_length=10,
                        null=True,
                        verbose_name="Спортивный разряд",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, default="users/avatar.jpg", upload_to="users/"
                    ),
                ),
                (
                    "discipline",
                    models.ForeignKey(
                        default="openfoil",
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        related_name="participants",
                        to="users.discipline",
                        to_field="slug",
                        verbose_name="Дисциплина",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "ordering": ["last_name", "first_name"],
            },
            managers=[
                ("objects", users.models.UserManager()),
            ],
        ),
    ]
