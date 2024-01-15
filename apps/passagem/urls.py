from django.urls import path
from .views import CriarPassagemView, ListarPassagensView, VerPassagensView

app_name = 'passagem'

urlpatterns = [
    path('criar/', CriarPassagemView.as_view(), name='criar_passagem'),
    path('listar_passagens/', ListarPassagensView.as_view(), name='listar_passagens'),
 path('ver_passagens/', VerPassagensView.as_view(), name='ver_passagens'),
]