from django.test import TestCase
from django.urls import reverse
from sitio_web.models import Producto, Contacto, Pedido

class ProductoListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        number_of_producto = 60

        for codigo_producto in range(number_of_producto):
            Producto.objects.create(
                nombre_producto=f'Torta {codigo_producto}',
                descripcion=f'Prueba {codigo_producto}',
                valor=10000,
            )
        
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/portal/producto/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('productos'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('productos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sitio_web/producto_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('productos'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['producto_list']) == 30)

    def test_lists_all_productos(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('productos')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['producto_list']) == 30)

class PedidoListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        number_of_pedido = 50

        for numero_pedido in range(number_of_pedido):
            Pedido.objects.create(
                nombre=f'Prueba {numero_pedido}',
                email='prueba@prueba',
                telefono=12345678,
                fecha='2020-11-25',
                descripcion=f'Prueba {numero_pedido}',
                valor=10000,
                estado='Ingresado',
            )
        
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/portal/pedido/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('pedidos'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('pedidos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sitio_web/pedido_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('pedidos'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['pedido_list']) == 30)

    def test_lists_all_pedidos(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('pedidos')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['pedido_list']) == 20)

class ProductoDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        number_of_producto = 31

        for codigo_producto in range(number_of_producto):
            Producto.objects.create(
                nombre_producto=f'Torta {codigo_producto}',
                descripcion=f'Prueba {codigo_producto}',
                valor=10000,
            )
        
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/portal/producto/3")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('producto-detail',args=[3]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('productos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sitio_web/producto_list.html')