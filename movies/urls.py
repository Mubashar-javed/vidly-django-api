from .views import MovieApiView
from django.urls import path

urlpatterns = [
    path('', MovieApiView.as_view())
]
