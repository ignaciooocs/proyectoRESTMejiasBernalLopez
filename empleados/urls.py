from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('empleadosListApi', views.lista_empleados),
    path('empleadosListApi/<int:pk>', views.detalle_empleado, name='empleado'),
    path('empleadosListApi/crear/', views.crear_empleado, name='crear_empleado'),
]
