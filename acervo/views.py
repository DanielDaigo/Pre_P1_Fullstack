from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm

def lista_livros(request):
    livros = Livro.objects.all()
    
    nome = request.GET.get('nome')
    tipo_acervo = request.GET.get('tipo_acervo')
    categoria = request.GET.get('categoria')
    
    if nome:
        livros = livros.filter(titulo__icontains=nome)
    if tipo_acervo:
        livros = livros.filter(tipo_acervo=tipo_acervo)
    if categoria:
        livros = livros.filter(categoria=categoria)
        
    context = {
        'livros': livros,
        'tipos_acervo': Livro.TIPO_ACERVO_CHOICES,
        'categorias': Livro.CATEGORIA_CHOICES,
    }
        
    return render(
        request, 
        'acervo/lista.html', 
        context
    )

def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()          # grava no banco PostgreSQL
            return redirect('lista')  # redireciona de volta para a lista
    else:
        form = LivroForm()       # requisição GET: formulário em branco
    
    return render(request, 'acervo/form.html', {'form': form})