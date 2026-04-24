import random
import uuid
from datetime import timedelta

from django.conf import settings
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
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(
        max_length=15, blank=True, null=True, unique=True, verbose_name="Телефон"
    )
    first_name = models.CharField(max_length=50, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=50, blank=True, verbose_name="Фамилия")
    avatar = models.ImageField(
        upload_to="avatars/", blank=True, null=True, verbose_name="Аватар"
    )
    is_active = models.BooleanField(default=False, verbose_name="Активен")
    is_staff = models.BooleanField(default=False, verbose_name="Персонал")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата регистрации"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["-created_at"]

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.email


class VerificationCode(models.Model):
    """Код подтверждения для регистрации/восстановления"""

    CODE_TYPE_CHOICES = [
        ("register", "Регистрация"),
        ("login", "Вход"),
        ("reset_password", "Сброс пароля"),
        ("verify_email", "Подтверждение почты"),
        ("verify_phone", "Подтверждение телефона"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="verification_codes",
    )
    code = models.CharField(max_length=6, verbose_name="Код")
    code_type = models.CharField(
        max_length=20,
        choices=CODE_TYPE_CHOICES,
        default="register",
        verbose_name="Тип кода",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    expires_at = models.DateTimeField(verbose_name="Действителен до")
    is_used = models.BooleanField(default=False, verbose_name="Использован")
    ip_address = models.GenericIPAddressField(
        blank=True, null=True, verbose_name="IP адрес"
    )

    class Meta:
        verbose_name = "Код подтверждения"
        verbose_name_plural = "Коды подтверждения"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["code", "is_used"]),
            models.Index(fields=["user", "code_type", "is_used"]),
        ]

    def __str__(self):
        return f"Code {self.code} for {self.user.email}"

    def is_expired(self):
        return timezone.now() > self.expires_at if self.expires_at else False

    def is_valid(self):
        return not self.is_used and not self.is_expired()

    @classmethod
    def generate_code(cls):
        """Генерация уникального 6-значного кода"""
        while True:
            code = str(random.randint(100000, 999999))
            if not cls.objects.filter(
                code=code, is_used=False, expires_at__gt=timezone.now()
            ).exists():
                return code

    @classmethod
    def create_for_user(cls, user, code_type="register", ip_address=None):
        """Создать новый код для пользователя"""
        # Деактивируем старые неиспользованные коды этого типа
        cls.objects.filter(
            user=user, code_type=code_type, is_used=False, expires_at__gt=timezone.now()
        ).update(is_used=True)

        code = cls.generate_code()
        expires_at = timezone.now() + timedelta(minutes=30)

        return cls.objects.create(
            user=user,
            code=code,
            code_type=code_type,
            expires_at=expires_at,
            ip_address=ip_address,
        )

    def send_email(self):
        """Отправка кода по email"""
        from django.core.mail import send_mail

        subject = f"Ваш код подтверждения: {self.code}"
        message = f"""
        Здравствуйте, {self.user.get_full_name() or self.user.email}!
        
        Ваш код подтверждения: {self.code}
        
        Код действителен 30 минут.
        
        Если вы не запрашивали этот код, просто проигнорируйте письмо.
        
        С уважением,
        Команда Fitness Club
        """

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [self.user.email],
            fail_silently=False,
        )


class BodyMetricSnapshot(models.Model):
    """
    Снимок параметров тела пользователя на определенную дату.
    Используется для истории прогресса и обучения ML.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="body_metrics",
        verbose_name="Пользователь",
    )
    recorded_date = models.DateField(
        verbose_name="Дата замера",
        help_text="Дата, когда были зафиксированы показатели",
    )

    # Основные показатели состава тела
    weight_kg = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Вес (кг)",
        help_text="Вес тела в килограммах (например, 75.50)",
    )
    body_fat_percent = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
        verbose_name="Процент жира (%)",
        help_text="Содержание жировой ткани в процентах",
    )
    muscle_mass_kg = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Мышечная масса (кг)",
        help_text="Масса скелетных мышц в килограммах",
    )

    # Антропометрия (объемы) — критично для фитнеса
    waist_cm = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
        blank=True,
        verbose_name="Обхват талии (см)",
    )
    chest_cm = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
        blank=True,
        verbose_name="Обхват груди (см)",
    )
    hips_cm = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
        blank=True,
        verbose_name="Обхват бедер (см)",
    )

    # Мета-данные
    source = models.CharField(
        max_length=20,
        choices=[
            ("manual", "Ручной ввод"),
            ("smart_scale", "Умные весы"),
            ("trainer", "Запись тренера"),
        ],
        default="manual",
        verbose_name="Источник данных",
    )
    notes = models.TextField(
        blank=True,
        verbose_name="Примечания",
        help_text="Комментарии пользователя или тренера к замеру",
    )

    class Meta:
        verbose_name = "Снимок прогресса"
        verbose_name_plural = "История прогресса"
        ordering = ["-recorded_date"]  # Сортировка: свежие сверху
        # Запрещаем два замера в один день для одного юзера (можно изменить под себя)
        constraints = [
            models.UniqueConstraint(
                fields=["user", "recorded_date"], name="unique_user_daily_metric"
            )
        ]
        indexes = [
            models.Index(
                fields=["user", "recorded_date"], name="idx_user_date_metrics"
            ),
        ]

    def __str__(self):
        return f"{self.user.username} — {self.recorded_date} ({self.weight_kg} кг)"
