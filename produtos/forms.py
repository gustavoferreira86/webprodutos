from django import forms
from crispy_forms.helper import FormHelper
from produtos.models import Produtos
from produtos.models import Fornecedores
from produtos.models import Categoria
import django_tables2 as tables

class SimpleTable(tables.Table):
    editable = tables.LinkColumn('edit_form',verbose_name='edit')
    class Meta:
        model = Produtos
        attrs = {'class': 'paleblue', }
        exclude = ['idprodutos']
		
class ProdutosForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    class Meta:
        model = Produtos
        exclude = ['idprodutos']

		
class FornecedoresForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    class Meta:
        model = Fornecedores
        exclude = ['idfornecedor'] 

class CategoriaForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    class Meta:
        model = Categoria
        exclude = ['idcategoria'] 

class EditarForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    class Meta:
        model = Produtos
        fields = ['precoproduto', 'fornecedores_idfornecedores']
		
		