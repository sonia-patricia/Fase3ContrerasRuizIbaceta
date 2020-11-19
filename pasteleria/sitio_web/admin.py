from django.contrib import admin

# Register your models here.
from . models import Producto, Contacto

admin.site.register(Producto)
admin.site.register(Contacto)
