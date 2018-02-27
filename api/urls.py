from rest_framework import routers

from api.views import MovieViewSet, GenreViewSet

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'genres', GenreViewSet)
urlpatterns = [
]
urlpatterns += router.urls
