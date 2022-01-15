from rest_framework.decorators import api_view
from rest_framework.response import Response
from menu.models import Menu, MenuMeal, MenuDrink
from menu.serializers import MenuSerializer, MenuMealSerializer, MenuDrinkSerializer


@api_view(['GET', 'POST'])
def menu_list(request):
    if request.method == 'GET':
        items = Menu.objects.order_by('pk')
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def menu_detail(request, pk):
    try:
        item = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = MenuSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MenuSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def menumeal_list(request):
    if request.method == 'GET':
        items = MenuMeal.objects.order_by('pk')
        serializer = MenuMealSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MenuMealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def menumeal_detail(request, pk):
    try:
        item = MenuMeal.objects.get(pk=pk)
    except MenuMeal.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = MenuMealSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MenuMealSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def menudrink_list(request):
    if request.method == 'GET':
        items = MenuDrink.objects.order_by('pk')
        serializer = MenuDrinkSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MenuDrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def menudrink_detail(request, pk):
    try:
        item = MenuDrink.objects.get(pk=pk)
    except MenuDrink.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = MenuDrinkSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MenuDrinkSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
