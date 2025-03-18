from django.views.generic import TemplateView, RedirectView
from django.templatetags.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.schemas import get_schema_view
from graphene_django.views import GraphQLView as BaseGraphQLView
from core.serializers import MyTokenObtainPairSerializer



# Create your views here.
class HomeView(TemplateView):
    """
    Returns an HTML page containing information about the API.
    """
    template_name = 'core/index.html'


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


class GraphQLView(BaseGraphQLView):
    """
    Wrapper for the GraphQL API.
    """
    graphiql = True


api_schema = get_schema_view(
    title='Pokemon API',
    description='This is an API that provides data on Pokemon.',
    version='1.0.0'
)


class FaviconRedirectView(RedirectView):
    """
    Redirects to the favicon.ico file.
    """
    url = static('images/favicon.ico')
    permanent = True
