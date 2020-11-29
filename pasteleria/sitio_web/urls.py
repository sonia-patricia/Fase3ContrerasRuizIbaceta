from django.urls import path, re_path
from sitio_web import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('contacto/', views.contacto, name='contacto'),

    path('portal/', views.portal, name='portal'),

    path('portal/producto/', views.ProductoListView.as_view(),
         name='productos'),  # Listado de productos
    path('portal/producto/<int:pk>', views.ProductoDetailView.as_view(),
         name='producto-detail'),  # Detalle del producto
    path('portal/producto/create/', views.ProductoCreate,
         name='producto_create'),  # Crear producto
    path('portal/producto/<int:pk>/update/', views.ProductoUpdate.as_view(),
         name='producto_update'),  # actualizar
    path('portal/producto/<int:pk>/delete/', views.ProductoDelete.as_view(),
         name='producto_delete'),  # eliminar

    path('portal/pedido/', views.PedidoListView.as_view(),
         name='pedidos'),  # Listado de pedidos
    path('portal/pedido/<int:pk>', views.PedidoDetailView.as_view(),
         name='pedido-detail'),  # Detalle del pedido
    path('portal/pedido/create/', views.PedidoCreate.as_view(),
         name='pedido_create'),  # Crear pedido
    path('portal/pedido/<int:pk>/update/', views.PedidoUpdate.as_view(),
         name='pedido_update'),  # actualizar
    path('portal/pedido/<int:pk>/delete/', views.PedidoDelete.as_view(),
         name='pedido_delete'),  # eliminar

    
     path('portal/usuario/', views.UserListView.as_view(),
         name='usuario'),  # Listado de usuarios
     path('portal/usuario/create/', views.UserCreate.as_view(),
         name='usuario_create'),  # Crear usuario
     
     path('portal/usuario/cambiar_clave/', views.change_password_view, name='cambiar_clave'),

     re_path(r'^portal/usuario/(?P<slug>[\w.@+-]+)/$', views.UserDetailView.as_view(),
         name='usuario-detail'),  # Detalle del usuario    
     re_path(r'^portal/usuario/(?P<slug>[\w.@+-]+)/update/$', views.UserUpdate.as_view(),
         name='usuario_update'),  # actualizar
     re_path(r'^portal/usuario/(?P<slug>[\w.@+-]+)/delete/$', views.UserDelete.as_view(),
         name='usuario_delete'),  # eliminar

    
]
