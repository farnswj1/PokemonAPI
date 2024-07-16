from django.urls import path
from core import views
from core.schemas import api_schema


app_name = 'core'

urlpatterns = [
    path('login', views.MyTokenObtainPairView.as_view(), name='login'),
    path('refresh', views.MyTokenRefreshView.as_view(), name='refresh'),
    path('docs', views.APIDocumentationView.as_view(), name='docs'),
    path('openapi', api_schema, name='openapi-schema'),
    path('graphql', views.APIGraphQLView.as_view(), name='graphql'),
]
