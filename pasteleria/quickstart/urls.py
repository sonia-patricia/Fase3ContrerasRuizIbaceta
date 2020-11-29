from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

#Importamos la app de django-rest
from rest_framework import routers
from quickstart import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
