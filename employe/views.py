from rest_framework.decorators import api_view
from rest_framework.response import Response
from employe.models import Employe
from employe.serializers import EmployeSerializer


@api_view(['GET', 'POST'])
def employe_list(request):
    if request.method == 'GET':
        items = Employe.objects.order_by('pk')
        serializer = EmployeSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def employe_detail(request, pk):
    try:
        item = Employe.objects.get(pk=pk)
    except Employe.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = EmployeSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
