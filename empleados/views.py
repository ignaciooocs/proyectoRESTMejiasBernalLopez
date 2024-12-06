from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list(request):
    return render(request, 'empleadosList.html')

def empleado(request, pk):  # Acepta el parámetro pk
    context = {'pk': pk}  # Puedes pasar el pk al template si es necesario
    return render(request, 'empleado.html', context)