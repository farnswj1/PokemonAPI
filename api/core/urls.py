from django.urls import path
from rest_framework.schemas import get_schema_view
from core import views

app_name = 'core'

schema = get_schema_view(
    title='Pokemon API',
    description='This is an API that provides data on Pokemon.',
    version='1.0.0'
)

urlpatterns = [
    path('login', views.MyTokenObtainPairView.as_view(), name='login'),
    path('refresh', views.MyTokenRefreshView.as_view(), name='refresh'),
    path('docs', views.APIDocumentationView.as_view(), name='docs'),
    path('openapi', schema, name='openapi-schema'),
]
