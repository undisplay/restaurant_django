from rest_framework.serializers import ModelSerializer
from food.models import Meal


class MealSerializer(ModelSerializer):

    class Meta:
        model = Meal
        depth = 2
        fields = '__all__'
