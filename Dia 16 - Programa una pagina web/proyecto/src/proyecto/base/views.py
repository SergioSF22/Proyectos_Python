from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Tarea


# Clase encargada de mostrar el Login
class Logueo(LoginView):
    template_name = 'base/login.html'
    fields = '__all__' # Indica que los campos del formulario son los atributos de la clase Tarea en .models.py
    redirect_authenticated_user = True # Indica que una vez logueado el usuario, se le va a redirigir

    # Función que indica donde redirigir al usuario una vez logueado
    def get_success_url(self):
        return reverse_lazy('tareas')


# Clase encargada de mostrar el registro de un nuevo usuario
class PaginaRegistro(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm # Define un formulario predeterminado
    redirect_authenticated_user = True # Indica que una vez logueado el usuario, se le va a redirigir
    success_url = reverse_lazy('tareas') # Cuando el formulario se completa, se vuelve a la página principal

    # Función encargada de validar el formulario de registro de un nuevo usuario
    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(PaginaRegistro, self).form_valid(form)

    # Función encargada de redirigir a un usuario ya autenticado a la pagina principal si este está logueado
    def get(self, *args, **kargs):
        if self.request.user.is_authenticated:
            return redirect('tareas')
        return super(PaginaRegistro, self).get(*args, **kargs)

# Clase encargada de mostrar la lista de tareas pendientes
class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = 'tareas' # Referencia interna al objeto

    # Función que obtiene el contexto de la sesión (usuario logueado, busqueda...), para así saber que tareas mostrar
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = context['tareas'].filter(usuario=self.request.user) # Usuario logueado
        context['count'] = context['tareas'].filter(completo=False).count() # Nº de tareas incompletas

        valor_buscado = self.request.GET.get('area-buscar') or '' # Almacena el valor búscado en la barra de búsqueda
        # Muestra las tareas filtrando el valor buscado
        if valor_buscado:
            context['tareas'] = context['tareas'].filter(titulo__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado
        return context


# Clase encargada de mostrar los detalles de una tarea
class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/tarea.html'


# Clase encargada de mostrar el formulario para crear una nueva tarea
class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo'] # Indica los campos del formulario
    success_url = reverse_lazy('tareas') # Cuando el formulario se completa, se vuelve a la página principal

    # Asigna valores por defecto al formulario de crear tarea
    def form_valid(self, form):
        form.instance.usuario = self.request.user # Asigna el nombre del usuario logueado al campo usuario del formulario
        return super(CrearTarea, self).form_valid(form)

# Clase encargada de editar una tarea existente
class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo'] # Indica los campos del formulario
    success_url = reverse_lazy('tareas') # Cuando el formulario se completa, se vuelve a la página principal


# Clase encargada de eliminar una tarea existente
class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea' # Referencia interna al objeto
    success_url = reverse_lazy('tareas') # Cuando el formulario se completa, se vuelve a la página principal


