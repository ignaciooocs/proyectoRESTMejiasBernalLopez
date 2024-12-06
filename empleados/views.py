from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import Empleado
from .serializers import EmpleadoSerializer
from django.shortcuts import render

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()  # Obtiene todos los empleados
    serializer_class = EmpleadoSerializer

@api_view(['GET'])
def lista_empleados(request):
    empleados = Empleado.objects.all()
    serializer = EmpleadoSerializer(empleados, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def detalle_empleado(request, pk):
    try:
        empleado = Empleado.objects.get(pk=pk)
    except Empleado.DoesNotExist:
        return Response({'error': 'Empleado no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmpleadoSerializer(empleado)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmpleadoSerializer(empleado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        empleado.delete()
        return Response({'mensaje': 'Empleado eliminado'}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def crear_empleado(request):
    if request.method == 'POST':
        serializer = EmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return render(request, 'index.html')