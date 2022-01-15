from rest_framework.serializers import ModelSerializer
from menu.models import Menu, MenuMeal, MenuDrink


class MenuSerializer(ModelSerializer):

    class Meta:
        model = Menu
        depth = 2
        fields = '__all__'


class MenuMealSerializer(ModelSerializer):

    class Meta:
        model = MenuMeal
        depth = 2
        fields = '__all__'


class MenuDrinkSerializer(ModelSerializer):

    class Meta:
        model = MenuDrink
        depth = 2
        fields = '__all__'
