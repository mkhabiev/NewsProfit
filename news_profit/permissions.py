from rest_framework import permissions
from news_profit.models import CLIENT


class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        else:
            return request.user.user_type == CLIENT