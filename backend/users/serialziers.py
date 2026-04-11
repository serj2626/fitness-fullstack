from rest_framework import serializers


from .models import CreateCodeSendEmail, User


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "email", "phone", ]


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "phone", "password", "password2"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("Пароли не совпадают")
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password")
        user = User.objects.create_user(password=password, **validated_data)
        return user


class SendCodeSerializer(serializers.ModelSerializer):
    code = serializers.CharField(read_only=True)

    class Meta:
        model = CreateCodeSendEmail
        fields = ["user", "code"]


class VerifyCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        code = attrs.get("code")
        code_obj = CreateCodeSendEmail.objects.filter(code=code, is_used=False).first()

        if not code_obj:
            raise serializers.ValidationError("Неверный код")
        if code_obj.is_expired():
            raise serializers.ValidationError("Срок действия кода истёк")

        attrs["code_obj"] = code_obj
        return attrs
