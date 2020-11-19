from django.urls import path
from sitio_web import views

urlpatterns=[
    path('',views.index,name='index'),
    path('catalogo/',views.catalogo,name='catalogo'),
    path('contacto/',views.contacto,name='contacto'),
    path('producto/', views.ProductoListView.as_view(), name = 'productos'), # Listado de productos 
    path('producto/<int:pk>', views.ProductoDetailView.as_view(), name='producto-detail'), # Detalle del producto
    path('producto/create/', views.ProductoCreate.as_view(), name='producto_create'), # Crear producto
    path('producto/<int:pk>/update/', views.ProductoUpdate.as_view(), name='producto_update'), # actualizar
    path('producto/<int:pk>/delete/', views.ProductoDelete.as_view(), name='producto_delete'),  # eliminar
]