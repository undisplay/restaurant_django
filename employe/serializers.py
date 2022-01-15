from rest_framework.serializers import ModelSerializer
from employe.models import Employe


class EmployeSerializer(ModelSerializer):

    class Meta:
        model = Employe
        depth = 2
        fields = '__all__'
