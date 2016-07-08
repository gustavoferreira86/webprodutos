from django import forms
from produtos.models import Produtos
from produtos.models import Fornecedores
from produtos.models import Categoria
				
class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos
        exclude = ['idprodutos'] 
		
class FornecedoresForm(forms.ModelForm):
    class Meta:
        model = Fornecedores
        exclude = ['idfornecedor'] 

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        exclude = ['idcategoria'] 

class EditarForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['precoproduto']
		
		