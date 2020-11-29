from django.test import TestCase
from sitio_web.forms import ProductoForm
from sitio_web.models import Producto

class ProductoFormsTest(TestCase):
    def test_valid_form(self):
        g = Producto.objects.create(
            nombre_producto='Torta Mil hojas', 
            descripcion='Torta para 15 personas',
            valor=15000)
        data = {'nombre_producto': g.nombre_producto, 
                'descripcion': g.descripcion,
                'valor': g.valor,}
        form = ProductoForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        g = Producto.objects.create(
            nombre_producto='', 
            descripcion='Torta para 15 personas',
            valor=15000)
        data = {'nombre_producto': g.nombre_producto, 
                'descripcion': g.descripcion,
                'valor': g.valor,}
        form = ProductoForm(data=data)
        self.assertFalse(form.is_valid())