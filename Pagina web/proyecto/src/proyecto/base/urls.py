from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Logueo, PaginaRegistro
from django.contrib.auth.views import LogoutView

# Contiene los paths de nuestra Vista web (enrutamientos)
urlpatterns = [path('', ListaPendientes.as_view(), name='tareas'), # Vista principal
               path('login/', Logueo.as_view(), name='login'), # Vista de logueo
               path('registro/', PaginaRegistro.as_view(), name='registro'), # Vista del registro de nuevos usuarios
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'), # Vista para desloguearse
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'), # Vista que muestra los detalles de una tarea
               path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'), # Vista con el formulario para crear una tarea
               path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'), # Vista para editar tarea existente
               path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea')] # Vista para editar tarea existente