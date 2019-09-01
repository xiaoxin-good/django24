from rest_framework.viewsets import ModelViewSet

from stuapp.models import Actor, Movie
from stuapp.serializers import ActorSerializer, MovieSerializer


class ActorView(ModelViewSet):
    """
    查询所有演员信息，增加、修改、删除演员信息
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieView(ModelViewSet):
    """
    查询所有影片信息，增加、修改、删除影片信息
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
