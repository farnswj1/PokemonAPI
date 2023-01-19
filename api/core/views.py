from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.serializers import MyTokenObtainPairSerializer


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    """
    Returns a pair of access and refresh tokens for the authenticated user.
    """
    serializer_class = MyTokenObtainPairSerializer


class MyTokenRefreshView(TokenRefreshView):
    """
    Returns a new access token for the authenticated user.
    """
    pass


class APIDocumentationView(TemplateView):
    """
    Returns an HTML page containing the auto-generated API documentation.
    """
    template_name = 'core/docs.html'
