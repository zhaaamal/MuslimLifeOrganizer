from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                # Разрешить все методы только для чтения (GET, HEAD, OPTIONS)
                return True
            return request.user.is_staff  # Разрешить действия создания, обновления и удаления только для администраторов
        return False


# *хотела попробовать для себя
