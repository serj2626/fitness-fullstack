# =============================================================================
# CORS & SESSIONS (КРИТИЧНО ДЛЯ NUXT 3)
# =============================================================================
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    # "https://your-frontend-domain.com",
]
CORS_ALLOW_METHODS = ["DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT"]
CORS_ALLOW_HEADERS = [
    "accept",
    "authorization",
    "content-type",
    "x-csrftoken",
    "x-requested-with",
]

# Куки сессии
SESSION_COOKIE_NAME = "sessionid"
SESSION_COOKIE_HTTPONLY = True  #  JS не читает (защита от XSS)
SESSION_COOKIE_SECURE = False  # True только на HTTPS в продакшене
SESSION_COOKIE_SAMESITE = "Lax"  # "None" если кросс-домен + Secure=True
SESSION_COOKIE_AGE = 1209600  # 2 недели

# CSRF настройки
CSRF_COOKIE_NAME = "csrftoken"
CSRF_COOKIE_HTTPONLY = False  #  JS ДОЛЖЕН читать токен для SPA
CSRF_COOKIE_SECURE = False  #  True только на HTTPS
CSRF_COOKIE_SAMESITE = "Lax"
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    # "https://your-frontend-domain.com",
]

AUTH_USER_MODEL = "users.User"
