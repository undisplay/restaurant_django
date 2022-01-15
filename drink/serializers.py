from rest_framework.serializers import ModelSerializer
from drink.models import Drink


class DrinkSerializer(ModelSerializer):

    class Meta:
        model = Drink
        depth = 2
        fields = '__all__'
