from rest_framework.serializers import ModelSerializer
from ordered.models import Ordered, DrinkOrderedLine, MealOrderedLine, MenuOrderedLine, WashOrderedLine


class OrderedSerializer(ModelSerializer):

    class Meta:
        model = Ordered
        depth = 2
        fields = '__all__'


class DrinkOrderedLineSerializer(ModelSerializer):

    class Meta:
        model = DrinkOrderedLine
        depth = 2
        fields = '__all__'


class MealOrderedLineSerializer(ModelSerializer):

    class Meta:
        model = MealOrderedLine
        depth = 2
        fields = '__all__'


class MenuOrderedLineSerializer(ModelSerializer):

    class Meta:
        model = MenuOrderedLine
        depth = 2
        fields = '__all__'


class WashOrderedLineSerializer(ModelSerializer):

    class Meta:
        model = WashOrderedLine
        depth = 2
        fields = '__all__'
