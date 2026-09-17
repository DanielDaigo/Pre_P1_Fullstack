from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm

def home(request):
    return render(request, 'acervo/home.html')

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
            form.save()
            return redirect('lista')
    else:
        form = LivroForm()
    
    return render(request, 'acervo/form.html', {'form': form, 'acao': 'Cadastrar'})

def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = LivroForm(instance=livro)
    
    return render(request, 'acervo/form.html', {'form': form, 'acao': 'Editar'})

def excluir_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('lista')
    
    return render(request, 'acervo/excluir.html', {'livro': livro})