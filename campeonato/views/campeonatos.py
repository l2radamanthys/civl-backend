from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from campeonato.models.campeonatos import Campeonato
from campeonato.serializers.campeonatos import CampeonatoSerializer

class CampeonatoViewSet(viewsets.ModelViewSet):
    queryset = Campeonato.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CampeonatoSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
