# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, TemplateView, UpdateView
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
	
def save(obj):
      context = super(EditTemplateView, self).get_context_data(**kwargs)
      context["form"].update()
      return render(context, Lista.as_view)

class EditTemplateView(TemplateView):
    template_name = "editar.html"
    form_class = EditarForm
    success_url = '/lista'
	
    def get_context_data(self, **kwargs):
     if self.request.method == 'GET':
        context = super(EditTemplateView, self).get_context_data(**kwargs)
        context['form'] = Produtos.objects.get(pk=self.kwargs.get('idprodutos', None))
        form = ProdutosForm(self.request.POST or None, instance=Produtos.objects.get(pk=self.kwargs.get('idprodutos', None)))  # instance= None
        context["form"] = form
        return context
     else:
      try:
          obj = Produto.objects.get(idprodutos=idprodutos)
          for key, value in updated_values.iteritems():
              setattr(obj, key, value)
          obj.save()
      except Produto.DoesNotExist:
          updated_values.update(obj)
          obj = Person(**updated_values)
          obj.save()
		  
class ContatoUpdateView(UpdateView):
 form_class = EditarForm
 model = Produtos
 success_url = '/lista/'
 template_name =  'editar.html'
 
 def get_success_url(self):
  return '/lista/'
		
class Lista(ListView):
        template_name = 'lista.html'
        model = Produtos
        context_object = 'nome'
        order_by = 'nomeproduto'
        def get_queryset(self):
         return Produtos.objects.all().order_by('nomeproduto')