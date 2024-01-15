from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def minha_view(request):
    imagem = AlgumaClasse.objects.get(pk=1)  # Substitua por sua lógica de obtenção de imagem
    return render(request, 'home.html', {'imagem': imagem})
