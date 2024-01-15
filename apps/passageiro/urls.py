from django.urls import path, include
from . import views
from rest_framework import routers
from .views import criar_passageiro, lista_passageiros

app_name = 'passageiro'

router = routers.DefaultRouter()
router.register('passageiros', views.PassageirosClassViewSet, basename='passageiros')

urlpatterns = [
    path('', include(router.urls)),
    path('criar/', criar_passageiro, name='criar_passageiro'),
    path('lista/', lista_passageiros, name='lista_passageiros'),
]