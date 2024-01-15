from django.urls import path, include
from . import views
from rest_framework import routers
from .views import criar_piloto, lista_pilotos

app_name = 'piloto'

router = routers.DefaultRouter()
router.register('pilotos', views.PilotosClassViewSet, basename='pilotos')

urlpatterns = [
    path('', include(router.urls) ),
    path('criar/', criar_piloto, name='criar_piloto'),
    path('lista/', lista_pilotos, name='lista_pilotos'),
]