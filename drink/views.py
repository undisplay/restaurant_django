from rest_framework.decorators import api_view
from rest_framework.response import Response
from drink.models import Drink
from drink.serializers import DrinkSerializer


@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        items = Drink.objects.order_by('pk')
        serializer = DrinkSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, pk):
    try:
        item = Drink.objects.get(pk=pk)
    except Drink.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = DrinkSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DrinkSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
