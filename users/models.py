"""Declare models for users app."""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError(_("Users must have an email address"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class Discipline(models.Model):
    """Модель дисциплины."""

    title = models.CharField(max_length=10)
    slug = models.SlugField(max_length=10, unique=True)
    # color = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.title


class User(AbstractUser):
    """Модель участника соревнований, он же пользователь сайта."""

    CATEGORY = [
        (None, "-"),
        ("1", "1й разряд"),
        ("2", "2й разряд"),
        ("3", "3й разряд"),
        ("КМС", "КМС"),
        ("МС", "МС"),
    ]

    username = None
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()
    sailnum = models.CharField(
        verbose_name="Номер на парусе", max_length=10, blank=True
    )
    discipline = models.ForeignKey(
        Discipline,
        verbose_name="Дисциплина",
        to_field="slug",
        default="openfoil",
        on_delete=models.SET_DEFAULT,
        related_name="participants",
    )
    trainer = models.CharField(
        verbose_name="Тренер", max_length=50, blank=True
    )
    club = models.CharField(verbose_name="Клуб", max_length=50, blank=True)
    city = models.CharField(verbose_name="Город", max_length=50)
    birthday = models.DateField(verbose_name="Дата рождения", null=True)
    category = models.CharField(
        verbose_name="Спортивный разряд",
        max_length=10,
        choices=CATEGORY,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name=_("Фото"),
        upload_to="users/",
        blank=True,
        default="users/avatar.jpg",
    )

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        return reverse("participant-details", kwargs={"pk": self.pk})

    def __str__(self):
        fullname = self.get_full_name()
        if fullname:
            return fullname
        return self.email
