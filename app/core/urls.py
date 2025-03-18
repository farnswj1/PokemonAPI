from django.urls import path, include
from core import views


app_name = 'core'

api_urls = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
    path('refresh/', views.MyTokenRefreshView.as_view(), name='refresh'),
    path('docs/', views.APIDocumentationView.as_view(), name='docs'),
    path('openapi/', views.api_schema, name='openapi-schema'),
]

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('api/', include((api_urls, 'api'), namespace='api')),
    path('graphql/', views.GraphQLView.as_view(), name='graphql'),
    path('favicon.ico', views.FaviconRedirectView.as_view(), name='favicon'),
]
