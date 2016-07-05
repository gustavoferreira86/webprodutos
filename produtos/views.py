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