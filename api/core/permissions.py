from django.http.request import HttpRequest
from django.views import View
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request: HttpRequest, view: View):
        return request.method in SAFE_METHODS or request.user.is_staff
