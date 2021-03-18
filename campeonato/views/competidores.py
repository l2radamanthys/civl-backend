from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from campeonato.models.competidores import Competidor
from campeonato.serializers.competidores import CompetidorSerializer

class CompetidorViewSet(viewsets.ModelViewSet):
    queryset = Competidor.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CompetidorSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
