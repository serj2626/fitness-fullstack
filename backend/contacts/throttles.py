from rest_framework.throttling import SimpleRateThrottle


class FeedbackThrottle(SimpleRateThrottle):
    """
    Ограничение: 2 запроса в минуту для обычных пользователей.
    Админы (is_staff) не ограничены.
    """

    scope = "feedback"

    def get_cache_key(self, request, view):
        if request.user and request.user.is_staff:
            return None
        if request.user and request.user.is_authenticated:
            return self.cache_format % {
                "scope": self.scope,
                "ident": request.user.pk,
            }
        return self.get_ident(request)
