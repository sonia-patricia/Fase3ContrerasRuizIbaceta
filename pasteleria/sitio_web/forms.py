from django import forms

from sitio_web.models import Producto


class ProductoForm(forms.ModelForm):

    nombre_producto = forms.CharField(
        label='Nombre del Producto',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    descripcion = forms.CharField(
        label='Descripción del Producto',
        max_length=1000,
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    valor = forms.IntegerField(
        label='Valor',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    class Meta:
        model = Producto
        fields = ('nombre_producto', 'descripcion', 'valor',)