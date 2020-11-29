from django.test import TestCase
from sitio_web.models import Producto

#comentario arreglo nombre git

class PastelesTestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Producto.objects.create(
            nombre_producto='TORTA ALEMANA DE CHOCOLATE Y ALMENDRAS', 
            descripcion='Torta par 10 personas',
            valor=15000)

    def test_tamano_nom(self):
        nom=Producto.objects.get(codigo_producto=1)
        max_length = nom._meta.get_field('nombre_producto').max_length
        self.assertGreaterEqual(100,max_length)