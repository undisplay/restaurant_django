from rest_framework.decorators import api_view
from rest_framework.response import Response
from wash.models import Wash
from wash.serializers import WashSerializer


@api_view(['GET', 'POST'])
def wash_list(request):
    if request.method == 'GET':
        items = Wash.objects.order_by('pk')
        serializer = WashSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WashSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def wash_detail(request, pk):
    try:
        item = Wash.objects.get(pk=pk)
    except Wash.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = WashSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WashSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
