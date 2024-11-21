from django.http.request import HttpRequest
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import APIView


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request: HttpRequest, view: APIView):
        return request.method in SAFE_METHODS or request.user.is_staff
