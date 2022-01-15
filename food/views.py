from rest_framework.decorators import api_view
from rest_framework.response import Response
from food.models import Meal
from food.serializers import MealSerializer


@api_view(['GET', 'POST'])
def meal_list(request):
    if request.method == 'GET':
        items = Meal.objects.order_by('pk')
        serializer = MealSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def meal_detail(request, pk):
    try:
        item = Meal.objects.get(pk=pk)
    except Meal.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = MealSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MealSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
