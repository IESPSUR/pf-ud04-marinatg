from django import forms
from django.forms import ModelForm
from .models import Producto, Marca, Vendido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class VendidoForm(forms.ModelForm):
    class Meta:
        model = Vendido
        fields = '__all__'
        """ModelForm para manipular un modelo, sino usar solo Form"""
