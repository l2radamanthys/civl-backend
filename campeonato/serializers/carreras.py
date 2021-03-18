from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from rest_framework_json_api.relations import ResourceRelatedField

from campeonato.models.carreras import Carrera


class CarreraSerializer(ModelSerializer):
    # model = ResourceRelatedField(many=False, read_only=True)

    class Meta:
        model = Carrera
        fields = (
            'nombre',
        )

    # included_serializers = {
    #     'user': UserSerializer,
    # }
