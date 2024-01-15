# apps/aviao/urls.py
from django.urls import path, include
from .views import criar_aviao, lista_avioes, aviao_detail, AvioesClassViewSet  # Adicione a importação correta
from rest_framework import routers

app_name = 'aviao'

router = routers.DefaultRouter()
router.register('avioes', AvioesClassViewSet, basename='avioes')  # Corrija a referência ao AvioesClassViewSet

urlpatterns = [
    path('avioes/', include(router.urls)),
    path('lista/', lista_avioes, name='lista_avioes'),
    path('criar/', criar_aviao, name='criar_aviao'),
    path('<int:aviao_id>/', aviao_detail, name='aviao_detail'),
    
]