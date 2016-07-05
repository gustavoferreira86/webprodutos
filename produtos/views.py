# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy

from produtos.models import Produtos
from produtos.models import Fornecedores
from produtos.models import Categoria
from produtos.forms import ProdutosForm
from produtos.forms import FornecedoresForm
from produtos.forms import CategoriaForm


def home(request):
        return render(request,'index.html')
		
def viewname(request):
    produtoid = request.GET['produtoid']
    produto = Produtos.objects.get(idprodutos=produtoid)
    return render(request, 'editar.html', {'produto': produto})

def objDetails(request, obj_id):
    try:
        produto = Produtos.objects.get(idproduto=obj_id)
    except produto.DoesNotExist:
        raise Http404
    return render(request, 'editar/', {'produto': produto})

class CriarProduto(CreateView):
	template_name = 'cadastro.html'
	model = Produtos
	form_class = ProdutosForm
	success_url = '/lista'
	
class CriarFornecedor(CreateView):
	template_name = 'cadastroFornecedor.html'
	model = Fornecedores
	form_class = FornecedoresForm
	success_url = '/cadastro'

class CriarCategoria(CreateView):
	template_name = 'cadastroCategoria.html'
	model = Categoria
	form_class = CategoriaForm
	success_url = '/cadastro'
		

class Lista(ListView):
        template_name = 'lista.html'
        model = Produtos
        context_object = 'nome'