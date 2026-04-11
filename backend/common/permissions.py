from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Разрешение: Изменение только для админов, чтение для всех.
    """

    def has_permission(self, request, view):
        # Безопасные методы (GET, HEAD, OPTIONS) доступны всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Для остальных методов (POST, PUT, PATCH, DELETE) нужен админ
        return request.user and request.user.is_staff


# class PermissionByReview(permissions.BasePermission):
#     """
#     Разрешение: создание только для авторизованных, чтение для всех, удаление только для админов
#     """

#     def has_permission(self, request, view):
#         # Безопасные методы (GET, HEAD, OPTIONS) доступны всем
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         # Для остальных методов (POST, PUT, PATCH, DELETE) нужен админ
#         return request.user
