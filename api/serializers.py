from rest_framework.serializers import ModelSerializer

from api.models import Movie, Genre


class MovieSerialzer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
