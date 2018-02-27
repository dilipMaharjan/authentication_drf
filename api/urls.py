from rest_framework import routers

from api.views import MovieViewSet, GenreViewSet

router = routers.DefaultRouter()
router.register(r'api/movies', MovieViewSet)
router.register(r'api/genres', GenreViewSet)
urlpatterns = [
]
urlpatterns += router.urls
