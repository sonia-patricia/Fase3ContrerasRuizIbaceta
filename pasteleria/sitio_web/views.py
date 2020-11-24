from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views import generic
from django.conf import settings
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from sitio_web.models import Contacto, Producto, Pedido
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(
        request,
        'index.html'
    )


def catalogo(request):
    return render(
        request,
        'productos.html'
    )


def contacto(request):

    if request.method == "POST":  # Cuando se presiona el boton enviar formulario

        # carga las variables con los campos del formulario
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        telefono = request.POST["telefono"]
        fecha = request.POST["fecha"]
        comment = request.POST["comentario"]
        radio = request.POST.get('optradio')

        contacto = Contacto(nombre=nombre,
                            email=email,
                            telefono=telefono,
                            fecha=fecha,
                            motivo=radio,
                            comentario=comment)
        contacto.save()  # Guarda en BD

        mostrar_popup = '1'

        return render(
            request,
            'formulario.html',
            context={'mostrar_popup': mostrar_popup}
        )

    else:

        return render(
            request,
            'formulario.html'
        )


def portal(request):
    return render(
        request,
        'portal.html'
    )


class ProductoListView(generic.ListView):
    model = Producto
    paginate_by = 30


class ProductoCreate(CreateView):
    model = Producto
    fields = ['nombre_producto', 'descripcion', 'valor']


class ProductoUpdate(UpdateView):
    model = Producto
    fields = ['nombre_producto', 'descripcion', 'valor']


class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos')


class ProductoDetailView(generic.DetailView):
    model = Producto


class PedidoListView(generic.ListView):
    model = Pedido
    paginate_by = 30


class PedidoCreate(CreateView):
    model = Pedido
    fields = ['nombre', 'email', 'telefono',
              'fecha', 'descripcion', 'valor', 'estado']


class PedidoUpdate(UpdateView):
    model = Pedido
    fields = ['nombre', 'email', 'telefono',
              'fecha', 'descripcion', 'valor', 'estado']


class PedidoDelete(DeleteView):
    model = Pedido
    success_url = reverse_lazy('pedidos')

class PedidoDetailView(generic.DetailView):
    model = Pedido

class UserListView(generic.ListView):
    model = User
    paginate_by = 30

class UserCreate(CreateView):
    model = User
    fields = ['username', 'email', 'first_name','last_name']
    template_name = '/auth/user_form.html'


class UserUpdate(UpdateView):
    model = User
    slug_field = "username"
    fields = ['username', 'email', 'first_name','last_name']


class UserDelete(DeleteView):
    model = User
    slug_field = "username"
    success_url = reverse_lazy('usuario')


class UserDetailView(generic.DetailView):
    model = User
    slug_field = "username"

def Cambiar_Clave(request):
    return render(
        request,
        'portal.html'
    )
