from rest_framework.viewsets import ModelViewSet

from api.models import Movie, Genre
from api.serializers import MovieSerialzer, GenreSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerialzer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
