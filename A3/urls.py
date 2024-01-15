"""A3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('pilotos/', include('piloto.urls', namespace='pilotos')),  # Alterado para namespace='pilotos'
    path('avioes/', include('aviao.urls', namespace='avioes')),  # Alterado para namespace='avioes'
    path('passagens/', include('passagem.urls', namespace='passagens')),  # Alterado para namespace='passagens'
    path('passageiros/', include('passageiro.urls', namespace='passageiros')),  # Alterado para namespace='passageiros'
    path('piloto/', include('piloto.urls', namespace='piloto')),  # Alterado para namespace='piloto'
    path('saiba_mais/', TemplateView.as_view(template_name='saiba_mais.html'), name='saiba_mais'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)