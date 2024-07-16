from django.views.generic import TemplateView
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from strawberry.django.views import GraphQLView
from core.serializers import MyTokenObtainPairSerializer
from core.schemas import graphql_schema


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


class APIGraphQLView(GraphQLView):
    """
    Wrapper for the GraphQL API.
    """
    @classmethod
    def as_view(cls, **kwargs):
        # Need to pass kwargs through as_view() to work properly
        graphql_ide = 'graphql_ide' if settings.DEBUG else None
        return super().as_view(
            schema=graphql_schema,
            graphql_ide=graphql_ide,
            **kwargs
        )
