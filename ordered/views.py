from rest_framework.decorators import api_view
from rest_framework.response import Response
from ordered.models import Ordered, DrinkOrderedLine, MealOrderedLine, MenuOrderedLine, WashOrderedLine
from ordered.serializers import OrderedSerializer, DrinkOrderedLineSerializer, MealOrderedLineSerializer, MenuOrderedLineSerializer, WashOrderedLineSerializer


@api_view(['GET', 'POST'])
def ordered_list(request):
    if request.method == 'GET':
        items = Ordered.objects.order_by('pk')
        serializer = OrderedSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def ordered_detail(request, pk):
    try:
        item = Ordered.objects.get(pk=pk)
    except Ordered.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = OrderedSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderedSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def drinkorderedline_list(request):
    if request.method == 'GET':
        items = DrinkOrderedLine.objects.order_by('pk')
        serializer = DrinkOrderedLineSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DrinkOrderedLineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def drinkorderedline_detail(request, pk):
    try:
        item = DrinkOrderedLine.objects.get(pk=pk)
    except DrinkOrderedLine.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = DrinkOrderedLineSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DrinkOrderedLineSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def mealorderedline_list(request):
    if request.method == 'GET':
        items = MealOrderedLine.objects.order_by('pk')
        serializer = MealOrderedLineSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MealOrderedLineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def mealorderedline_detail(request, pk):
    try:
        item = MealOrderedLine.objects.get(pk=pk)
    except MealOrderedLine.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = MealOrderedLineSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MealOrderedLineSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def menuorderedline_list(request):
    if request.method == 'GET':
        items = MenuOrderedLine.objects.order_by('pk')
        serializer = MenuOrderedLineSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MenuOrderedLineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def menuorderedline_detail(request, pk):
    try:
        item = MenuOrderedLine.objects.get(pk=pk)
    except MenuOrderedLine.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = MenuOrderedLineSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MenuOrderedLineSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def washorderedline_list(request):
    if request.method == 'GET':
        items = WashOrderedLine.objects.order_by('pk')
        serializer = WashOrderedLineSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WashOrderedLineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def washorderedline_detail(request, pk):
    try:
        item = WashOrderedLine.objects.get(pk=pk)
    except WashOrderedLine.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = WashOrderedLineSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WashOrderedLineSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
