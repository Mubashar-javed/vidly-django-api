from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import MovieViewSet, GenreApiView

router = DefaultRouter(trailing_slash=False)
router.register(r'movies', MovieViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('genres', GenreApiView.as_view())
]
