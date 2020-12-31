from dj_rest_auth.views import LoginView
from django.urls import path

urlpatterns = [
    path("auth", LoginView.as_view()),
]
