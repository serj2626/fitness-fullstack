from django.core.cache import cache
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
import json
import requests

class LoginProtectionMiddleware(MiddlewareMixin):
    """
    Middleware для защиты от брутфорса на эндпоинте /api/auth/login/
    """

    def process_request(self, request):
        if request.path == "/api/auth/login/" and request.method == "POST":
            ip = self.get_client_ip(request)
            key = f"login_attempts:{ip}"
            attempts = cache.get(key, 0)

            # Если уже было 3+ неудачных попытки → требуем капчу
            if attempts >= 3:
                data = json.loads(request.body.decode("utf-8") or "{}")
                if "captcha" not in data or not self.verify_captcha(data["captcha"]):
                    return JsonResponse(
                        {"detail": "Captcha required"}, status=429
                    )

    def process_response(self, request, response):
        if request.path == "/api/auth/login/" and request.method == "POST":
            ip = self.get_client_ip(request)
            key = f"login_attempts:{ip}"

            if response.status_code != 200:  # неудачный логин
                attempts = cache.get(key, 0) + 1
                cache.set(key, attempts, timeout=60)  # сброс через 1 минуту
            else:
                cache.delete(key)  # удачный вход — сбрасываем счетчик

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")

    def verify_captcha(self, token: str) -> bool:
        """
        Проверка Google reCAPTCHA (v2/v3)
        """
        import requests
        from django.conf import settings

        secret_key = settings.RECAPTCHA_SECRET_KEY
        url = "https://www.google.com/recaptcha/api/siteverify"
        data = {"secret": secret_key, "response": token}
        r = requests.post(url, data=data).json()
        return r.get("success", False)
