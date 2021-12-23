
from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("login", views.MyTokenObtainPairView.as_view(), name="login"),
    path("refresh", views.MyTokenRefreshView.as_view(), name="refresh"),
]
