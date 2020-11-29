from django.test import TestCase
from sitio_web.models import Producto

#comentario arreglo nombre git

class PastelesTestCase(TestCase):
    def setup(self):
        a1=Producto.objects.create(nombre_producto='TORTA ALEMANA DE CHOCOLATE Y ALMENDRAS')
        Producto.objects.create(nombre_producto=a1, Descripcion='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi convallis.', valor=9990)

    def test_tamano_nom(self):
        nom=Producto.objects.get(codigo_producto=1)
        max_length = nom._meta.get_field('nombre_producto').max_length
        self.assertEquals(max_length,100)