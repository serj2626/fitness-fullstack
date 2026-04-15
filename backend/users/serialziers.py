from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import VerificationCode

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователя (для отображения)"""

    full_name = serializers.CharField(source="get_full_name", read_only=True)
    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "phone",
            "first_name",
            "last_name",
            "full_name",
            "avatar",
            "avatar_url",
            "is_active",
        ]
        read_only_fields = ["id", "is_active", "created_at", "updated_at"]

    def get_avatar_url(self, obj):
        if obj.avatar:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.avatar.url)
        return None


class RegisterRequestSerializer(serializers.Serializer):
    """Запрос на регистрацию (отправка кода)"""

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    phone = serializers.CharField(max_length=15, required=False, allow_blank=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Пользователь с таким email уже существует"
            )
        return value


class RegisterVerifySerializer(serializers.Serializer):
    """Подтверждение регистрации кодом"""

    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)
    first_name = serializers.CharField(max_length=50, required=False)
    last_name = serializers.CharField(max_length=50, required=False)
    password = serializers.CharField(
        max_length=128, write_only=True, validators=[validate_password]
    )
    password_confirm = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError(
                {"password_confirm": "Пароли не совпадают"}
            )

        # Проверка кода
        try:
            user = User.objects.get(email=attrs["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError({"email": "Пользователь не найден"})

        try:
            verification_code = VerificationCode.objects.filter(
                user=user, code=attrs["code"], code_type="register", is_used=False
            ).latest("created_at")
        except VerificationCode.DoesNotExist:
            raise serializers.ValidationError({"code": "Неверный или истёкший код"})

        if not verification_code.is_valid():
            raise serializers.ValidationError({"code": "Код истёк или уже использован"})

        attrs["user"] = user
        attrs["verification_code"] = verification_code
        return attrs

    def create(self, validated_data):
        user = validated_data["user"]
        verification_code = validated_data["verification_code"]

        user.first_name = validated_data.get("first_name", "")
        user.last_name = validated_data.get("last_name", "")
        user.set_password(validated_data["password"])
        user.is_active = True
        user.save()

        # Помечаем код как использованный
        verification_code.is_used = True
        verification_code.save()

        return user


class LoginRequestSerializer(serializers.Serializer):
    """Запрос на вход (отправка кода)"""

    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
            if not user.is_active:
                raise serializers.ValidationError("Пользователь не активирован")
        except User.DoesNotExist:
            # Не показываем существует ли пользователь (безопасность)
            pass
        return value


class LoginVerifySerializer(serializers.Serializer):
    """Подтверждение входа кодом"""

    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        try:
            user = User.objects.get(email=attrs["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError({"email": "Неверные учётные данные"})

        try:
            verification_code = VerificationCode.objects.filter(
                user=user, code=attrs["code"], code_type="login", is_used=False
            ).latest("created_at")
        except VerificationCode.DoesNotExist:
            raise serializers.ValidationError({"code": "Неверный или истёкший код"})

        if not verification_code.is_valid():
            raise serializers.ValidationError({"code": "Код истёк или уже использован"})

        attrs["user"] = user
        attrs["verification_code"] = verification_code
        return attrs

    def create(self, validated_data):
        user = validated_data["user"]
        verification_code = validated_data["verification_code"]

        verification_code.is_used = True
        verification_code.save()

        return user


class PasswordResetRequestSerializer(serializers.Serializer):
    """Запрос на сброс пароля"""

    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
            if not user.is_active:
                raise serializers.ValidationError("Пользователь не активирован")
        except User.DoesNotExist:
            pass  # Не показываем существует ли пользователь
        return value


class PasswordResetVerifySerializer(serializers.Serializer):
    """Подтверждение сброса пароля"""

    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)
    new_password = serializers.CharField(max_length=128, validators=[validate_password])
    new_password_confirm = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs["new_password"] != attrs["new_password_confirm"]:
            raise serializers.ValidationError(
                {"new_password_confirm": "Пароли не совпадают"}
            )

        try:
            user = User.objects.get(email=attrs["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError({"email": "Пользователь не найден"})

        try:
            verification_code = VerificationCode.objects.filter(
                user=user, code=attrs["code"], code_type="reset_password", is_used=False
            ).latest("created_at")
        except VerificationCode.DoesNotExist:
            raise serializers.ValidationError({"code": "Неверный или истёкший код"})

        if not verification_code.is_valid():
            raise serializers.ValidationError({"code": "Код истёк или уже использован"})

        attrs["user"] = user
        attrs["verification_code"] = verification_code
        return attrs

    def create(self, validated_data):
        user = validated_data["user"]
        verification_code = validated_data["verification_code"]

        user.set_password(validated_data["new_password"])
        user.save()

        verification_code.is_used = True
        verification_code.save()

        return user


class ChangePasswordSerializer(serializers.Serializer):
    """Смена пароля для авторизованного пользователя"""

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
    new_password_confirm = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        if attrs["new_password"] != attrs["new_password_confirm"]:
            raise serializers.ValidationError(
                {"new_password_confirm": "Пароли не совпадают"}
            )

        user = self.context["request"].user
        if not user.check_password(attrs["old_password"]):
            raise serializers.ValidationError(
                {"old_password": "Неверный текущий пароль"}
            )

        attrs["user"] = user
        return attrs

    def save(self):
        user = self.validated_data["user"]
        user.set_password(self.validated_data["new_password"])
        user.save()
        return user
