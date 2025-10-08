# core/views.py
from django.shortcuts import render
# Lembre-se, use o nome da classe correto: Cliente
from .models import Cliente 

def index(request):
    # CORREÇÃO 1: Precisa do método .all() para buscar todos os objetos
    clientes = Cliente.objects.all() 
    
    # CORREÇÃO 2: A função render() é chamada com parênteses, não chaves.
    context = {'clientes': clientes}
    
    # Renderiza o template 'index.html' passando o dicionário de contexto.
    return render(request, 'index.html', context)