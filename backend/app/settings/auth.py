# ✅ CORS: разрешаем Nuxt (с куками!)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Nuxt в деве
]
CORS_ALLOW_CREDENTIALS = True  # 🔥 ВАЖНО: разрешаем куки

# ✅ CSRF: доверяем Nuxt
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
]
CSRF_COOKIE_SAMESITE = 'Lax'   # или 'None' если HTTPS
CSRF_COOKIE_HTTPONLY = False   # 🔥 Nuxt должен читать CSRF-токен

# ✅ Сессии (уже включены по умолчанию, но проверь)
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_HTTPONLY = True  # JS не видит sessionid (безопасно)
SESSION_COOKIE_SECURE = False   # True только на HTTPS

AUTH_USER_MODEL = "users.User"