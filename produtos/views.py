# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, TemplateView
from django.core.urlresolvers import reverse_lazy

from produtos.models import Produtos
from produtos.models import Fornecedores
from produtos.models import Categoria
from produtos.forms import ProdutosForm
from produtos.forms import FornecedoresForm
from produtos.forms import CategoriaForm
from produtos.forms import EditarForm

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


class EditarProduto(CreateView):
	template_name = 'editar.html'
	model = Produtos
	form_class = EditarForm
	success_url = '/lista'
	
def save(self, **kwargs):
        mfields = iter(self._meta.fields)
        mods = [(f.attname, kwargs[f.attname]) for f in mfields if f.attname in kwargs]
        for fname, fval in mods: setattr(self, fname, fval)
        return super(PendingDeprecationWarning, self).save()	

class EditTemplateView(TemplateView):
    template_name = "editar.html"
    form_class = EditarForm
	
    def get_context_data(self, **kwargs):
        context = super(EditTemplateView, self).get_context_data(**kwargs)
        context['form'] = Produtos.objects.get(pk=self.kwargs.get('idproduto', None))
        form = EditarForm(self.request.POST or None, instance=Produtos.objects.get(pk=self.kwargs.get('idproduto', None)))  # instance= None
        context["form"] = form
        return context
    def saveProduto(self, request, pk):
        return redirect('/lista')
	
class Lista(ListView):
        template_name = 'lista.html'
        model = Produtos
        context_object = 'nome'