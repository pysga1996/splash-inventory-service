from django.views.decorators.http import require_http_methods
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import CustomerPoint
from main.serializers import CustomerPointSerializer


# Create your views here.

@api_view(['GET', 'POST'])
@require_http_methods(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def customer_point_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    match request.method:
        case 'GET':
            customer_points = CustomerPoint.objects.all()
            serializer = CustomerPointSerializer(customer_points, many=True)
            return Response(serializer.data)
        case 'POST':
            serializer = CustomerPointSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@require_http_methods(['GET', 'POST', 'PUT', 'DELETE'])
def customer_point_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        customer_point = CustomerPoint.objects.get(pk=pk)
    except CustomerPoint.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    match request.method:
        case 'GET':
            serializer = CustomerPointSerializer(customer_point)
            return Response(serializer.data)
        case 'PUT':
            serializer = CustomerPointSerializer(customer_point, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        case 'DELETE':
            customer_point.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
