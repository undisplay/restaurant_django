from rest_framework.serializers import ModelSerializer
from wash.models import Wash


class WashSerializer(ModelSerializer):

    class Meta:
        model = Wash
        depth = 2
        fields = '__all__'
