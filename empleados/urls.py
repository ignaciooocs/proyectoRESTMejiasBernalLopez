# empleados/urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .views import EmpleadoViewSet

# Crear el router
router = DefaultRouter()
router.register(r'empleados', EmpleadoViewSet, basename='empleado')

# Las vistas tradicionales, como la página de inicio y los botones
urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('empleadosListApi/', views.lista_empleados, name='empleados_list'),  # Lista empleados JSON
    path('empleadosListApi/<int:pk>', views.detalle_empleado, name='empleado'),  # Detalle de un empleado
    path('empleadosListApi/crear/', views.crear_empleado, name='crear_empleado'),  # Crear empleado
]

# Incluir las URLs generadas por el router
urlpatterns += router.urls

