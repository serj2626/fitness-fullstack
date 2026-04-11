import random
import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone=None, password=None, **extra_fields):
        if not email:
            raise ValueError("Email обязателен")
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(
        max_length=15, blank=True, null=True, unique=True, verbose_name="Телефон"
    )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class CreateCodeSendEmail(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    code = models.CharField(max_length=6, verbose_name="Код", unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_used = models.BooleanField(default=False, verbose_name="Использован")

    class Meta:
        verbose_name = "Код подтверждения"
        verbose_name_plural = "Коды подтверждения"
        indexes = [models.Index(fields=["code", "is_used"])]

    def is_expired(self):
        if not self.created_at:
            return True
        return timezone.now() > self.created_at + timezone.timedelta(minutes=30)

    def save(self, *args, **kwargs):
        # Генерируем код только при создании нового объекта
        if not self.code and not self.pk:
            while True:
                self.code = str(random.randint(100000, 999999))
                if not CreateCodeSendEmail.objects.filter(code=self.code).exists():
                    break
        super().save(*args, **kwargs)
